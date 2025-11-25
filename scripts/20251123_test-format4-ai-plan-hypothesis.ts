import { Pool } from 'pg';
import * as dotenv from 'dotenv';
import * as fs from 'fs';
import * as path from 'path';
import { createGateway, generateText } from 'ai';

// Load environment from .env.vercel (with override to ensure it takes precedence over .env)
dotenv.config({ path: path.join(__dirname, '..', '.env.vercel'), override: true });

// ============================================================================
// Configuration
// ============================================================================

const MODEL_NAME = 'google/gemini-3.0-pro-preview';
const MAX_OUTPUT_TOKENS = 64000; // Gemini 3.0 Pro max output limit
const TOKENS_PER_BATCH = 700000; // Target tokens per batch (留保分を考慮)
const ESTIMATED_PROMPT_OVERHEAD = 100000; // Prompt template overhead
const PROMPT_VERSION = 'format4-by-hypothesis'; // Update this when changing the prompt

// ============================================================================
// Prompt Templates
// ============================================================================

// Initial report generation prompt
const INITIAL_PROMPT_TEMPLATE = `あなたは法案に関する市民との対話セッションを分析し、横断的な考察を行う専門家です。
下記の情報を元に、対話セッションのまとめレポートを作成してください。

## 法案の背景

以下は「{{interviewTitle}}」というテーマで実施された対話セッションの分析依頼です。

【法案の概要】
{{interviewDescription}}

{{interviewOverview}}

【主なポイント】
{{interviewThemes}}

【対話で扱った質問】
{{interviewQuestions}}

【参考情報・詳細】
{{knowledgeContext}}

この対話は上記の背景、質問、参考情報に基づいて実施されました。この文脈を踏まえて、以下のセッションデータを分析してください。

---

## あなたのタスク

下記の対話セッション（{{sessionCount}}セッション）を横断的に分析し、法案に対する市民の意見、懸念、提案、質問などを整理してMarkdownレポートを生成してください。

注意: これは初回レポート生成です。後ほど追加のセッションデータを統合する予定なので、現時点でのデータに基づいた分析を提供してください。

## 出力フォーマット

# {{interviewTitle}} - 市民対話レポート

## まとめ

[全体を通じて見えてきた主要なテーマ、パターン、重要な発見を2-3段落で要約してください。]

## 主要な論点

### 論点1: [法案に対する主要な論点名]

#### 賛成意見・期待される効果
- [意見1]
- [意見2]

#### 懸念・反対意見
- [懸念1]
- [懸念2]

#### 提案・アイデア
- [提案1]
- [提案2]

### 論点2: [法案に対する主要な論点名]

[同様に、対話から抽出された主要な論点ごとに章立てして分析結果を記述してください]

## よくある質問と市民の疑問

[対話セッションで頻繁に出た質問や疑問点をまとめてください]

## 影響を受けるステークホルダーの視点

[異なるステークホルダー（事業者、消費者、行政など）の視点から見た意見をまとめてください]

---

重要な注意事項:
1. Markdownフォーマットで出力してください
2. HTMLタグは使用しないでください
3. 太字マークダウン（アスタリスク2つ）は使用しないでください。日本語では括弧の処理がうまくいかないことが多いためです
4. 前置きや説明は不要で、「# {{interviewTitle}} - 市民対話レポート」から始めてください
5. 具体的な発言を引用する場合は、必ず「#」を付けたセッション番号で出典を明記してください
6. 個々のセッションの要約ではなく、横断的な分析に焦点を当ててください
7. 【重要】対話参加者の生の声を積極的に引用してください。「"発言内容"(#セッション番号)」の形式で多数引用することで、リアリティと説得力のあるレポートにしてください
8. 【重要】対話参加者の数量的情報や量的表現は一切含めないでください。以下のような表現は使用禁止です：
   - 禁止例: 「多くの参加者が」「一部の人が」「ほとんどの人が」「大半が」「少数だが」
   - 推奨: 「ある参加者は」「〜という意見がある」「〜という視点も示された」など
9. 【重要】価値判断や評価を含む表現を避けてください。以下のような表現は使用禁止です：
   - 禁止例: 「さらに踏み込み」「より高度な」「深い洞察」「優れた提案」「重要度が高い」
   - 推奨: 「〜という意見がある」「〜という視点も示された」など、中立的な記述を使用
10. 【重要】レトリックや主観的な修飾語を排除し、学術論文のように客観的かつ簡潔に記述してください
11. 【重要】表面的な議論にとどまらないように、意見に対する反論や再反論なども積極的に構造化しながら取り上げてください
12. {{outputLengthGuidance}}

---

## セッションデータ ({{sessionCount}}セッション)

{{sessionsData}}
`;

// Incremental update prompt
const UPDATE_PROMPT_TEMPLATE = `あなたは複数のインタビューセッションを分析し、横断的な考察を行う専門家です。

## タスク概要

以前に作成した集約レポートに、**追加のセッションデータ（{{newSessionCount}}セッション）を統合**して、レポートを更新してください。

**重要**: 最終的なレポートには、どのデータが「新しく追加された」か、「前回のレポートから」といった記述は一切含めないでください。すべてのセッションを一度に分析したかのように、一つの統合されたレポートとして出力してください。

## インタビューの背景

以下は「{{interviewTitle}}」というテーマで実施されたインタビューの分析です。

【説明】
{{interviewDescription}}

【概要】
{{interviewOverview}}

【主なテーマ】
{{interviewThemes}}

【インタビューで扱った質問】
{{interviewQuestions}}

【参考知識・コンテキスト】
{{knowledgeContext}}

---

## 前回のレポート

以下は、これまでに分析したセッションから作成したレポートです：

{{previousReport}}

---

## 新しいセッションデータ ({{newSessionCount}}セッション)

以下の新しいセッションを分析し、上記のレポートに統合してください：

{{sessionsData}}

---

## あなたのタスク

1. 追加のセッションデータを分析し、前回のレポートに含まれていない発見、視点、パターンを特定してください
2. 前回のレポートを更新してください：
   - 新しい発見があれば、該当するカテゴリに追加
   - 新しいカテゴリが必要であれば追加
   - 既存の記述が追加データで補強される場合は、引用を追加
   - 「まとめ」セクションも追加データを反映して更新
3. 前回のレポートの良い部分は維持してください（不要な削除や書き換えは避ける）

**絶対に守るべきルール:**
- 「新たなセッションデータにより」「追加のデータから」「前回のレポートでは」といった、分析プロセスを示唆する表現は一切使用しないでください
- 「より具体的な」「さらに詳細な」など、レポートの更新履歴を示す表現も避けてください
- すべてのセッションを最初から一度に分析したかのように記述してください
- 引用を追加する場合も、必ず「#」を付けたセッション番号で出典を明記してください
- 前回のレポートの構造とスタイルを維持してください
- 前置きや説明は不要で、更新された「# {{interviewTitle}} - 集約レポート」を直接出力してください

注意事項:
1. Markdownフォーマットで出力してください
2. HTMLタグは使用しないでください
3. 太字マークダウン（アスタリスク2つ）は使用しないでください。日本語では括弧の処理がうまくいかないことが多いためです
4. 具体的な発言を引用する場合は、必ず「#」を付けたセッション番号で出典を明記してください
5. 【重要】インタビュー参加者の生の声を積極的に引用してください。「"発言内容"(#セッション番号)」の形式で引用してください
6. 【重要】数量的情報や量的表現は一切含めないでください (「多くの参加者が」「一部の人が」など禁止)
7. 【重要】価値判断や評価を含む表現を避けてください (「深い洞察」「優れた提案」など禁止)
8. 【重要】レトリックや主観的な修飾語を排除し、学術論文のように客観的かつ簡潔に記述してください
9. {{outputLengthGuidance}}

---

更新されたレポートを出力してください：
`;

// Parallel merge prompt - merges multiple independent batch reports into one
const MERGE_PROMPT_TEMPLATE = `あなたは複数のインタビューセッションを分析し、横断的な考察を行う専門家です。

## タスク概要

複数のバッチに分けて並列に分析されたインタビューレポートを、**一つの統合されたレポート**にマージしてください。

## インタビューの背景

以下は「{{interviewTitle}}」というテーマで実施されたインタビューの分析です。

【説明】
{{interviewDescription}}

【概要】
{{interviewOverview}}

【主なテーマ】
{{interviewThemes}}

【インタビューで扱った質問】
{{interviewQuestions}}

【参考知識・コンテキスト】
{{knowledgeContext}}

---

## バッチレポート ({{batchCount}}個のレポート)

以下は、セッションを{{batchCount}}個のバッチに分けて並列に分析した結果です：

{{batchReports}}

---

## あなたのタスク

上記の{{batchCount}}個のレポートを統合し、一つの包括的な集約レポートを作成してください。

**重要な注意事項:**
1. **情報の完全保持**: マージ前のレポートにあった情報を失わないでください。すべての重要な発見、指摘、引用を統合レポートに含めてください
2. **生の引用をそのまま引き継ぐ**: 各バッチレポートに含まれる具体的な発言の引用は、セッション番号とともにそのまま統合レポートに含めてください
3. **重複の排除**: 複数のバッチで同じ発見や意見が記載されている場合のみ、一度だけ記載してください。ただし引用は異なるセッションからのものであれば複数残してください
4. **カテゴリの再構成**: バッチごとのカテゴリを見直し、より適切な分類に再構成してください
5. **網羅性の確保**: すべてのバッチから重要な発見を漏らさず含めてください。マージ前のレポートで言及されていた論点や視点がすべて統合レポートに反映されているか確認してください
6. **一貫性の維持**: トーンやスタイルを統一し、一つのレポートとして自然に読めるようにしてください
7. **文字数について**: 情報を保持するために文字数が増えることは問題ありません。包括的で詳細なレポートを作成してください

**絶対に守るべきルール:**
- 「バッチ1では」「バッチ2の分析によると」といった、バッチ分割を示唆する表現は一切使用しないでください
- すべてのセッションを最初から一度に分析したかのように記述してください
- 引用する場合も、必ず「#」を付けたセッション番号で出典を明記してください
- Markdownフォーマットで出力してください
- HTMLタグは使用しないでください
- 太字マークダウン（アスタリスク2つ）は使用しないでください
- 前置きや説明は不要で、「# {{interviewTitle}} - 集約レポート」から始めてください
- 数量的情報や量的表現は一切含めないでください (「多くの参加者が」など禁止)
- 価値判断や評価を含む表現を避けてください (「深い洞察」など禁止)
- レトリックや主観的な修飾語を排除し、学術論文のように客観的かつ簡潔に記述してください
- {{outputLengthGuidance}}

## 出力フォーマット

# {{interviewTitle}} - 集約レポート

## まとめ

[全体を通じて見えてきた主要なテーマ、パターン、重要な発見を2段落で要約してください。]

## 仮説1: [事前に設定した仮説]

### 支持する意見
- [意見1]
- [意見2]

### 反論・異なる視点
- [反論1]
- [反論2]

### 検証結果
[この仮説に対する総合的な評価]

## 仮説2: [事前に設定した仮説]

[同様に、事前に設定した仮説ごとに章立てして検証結果を記述してください]

---

統合されたレポートを出力してください：
`;

// ============================================================================
// Helper Functions
// ============================================================================

function estimateTokens(text: string): number {
  // Rough estimation: 1 token ≈ 4 characters (for Japanese/English mix)
  return Math.ceil(text.length / 4);
}

interface SessionData {
  id: string;
  sessionNumber: number;
  messages: Array<{
    role: 'user' | 'assistant';
    content: string;
    timestamp: string;
  }>;
}

async function fetchSessionData(
  pool: Pool,
  slug: string,
  sessionIds: string[]
): Promise<SessionData[]> {
  if (sessionIds.length === 0) return [];

  console.log(`📥 Fetching ${sessionIds.length} sessions from production...`);

  // Query 1: Get session metadata
  const sessionsResult = await pool.query(`
    SELECT id, session_number
    FROM interview_sessions
    WHERE id = ANY($1) AND slug = $2
    ORDER BY session_number ASC
  `, [sessionIds, slug]);

  const sessionMap = new Map(
    sessionsResult.rows.map(row => [row.id, {
      id: row.id,
      sessionNumber: row.session_number || 0
    }])
  );

  // Query 2: Get all messages
  const messagesResult = await pool.query(`
    SELECT session_id, role, content, timestamp
    FROM messages
    WHERE session_id = ANY($1)
    ORDER BY session_id, timestamp ASC
  `, [sessionIds]);

  // Group messages by session_id
  const messagesBySession = new Map<string, Array<{
    role: 'user' | 'assistant';
    content: string;
    timestamp: string;
  }>>();

  for (const row of messagesResult.rows) {
    if (!messagesBySession.has(row.session_id)) {
      messagesBySession.set(row.session_id, []);
    }
    messagesBySession.get(row.session_id)!.push({
      role: row.role as 'user' | 'assistant',
      content: row.content,
      timestamp: row.timestamp
    });
  }

  // Combine data
  const sessionsData: SessionData[] = [];
  for (const sessionId of sessionIds) {
    const session = sessionMap.get(sessionId);
    const messages = messagesBySession.get(sessionId) || [];
    if (session && messages.length > 0) {
      sessionsData.push({
        id: session.id,
        sessionNumber: session.sessionNumber,
        messages
      });
      console.log(`   ✓ Session #${session.sessionNumber}: ${messages.length} messages`);
    }
  }

  return sessionsData;
}

function formatSessionsData(sessions: SessionData[]): string {
  return sessions.map(session => {
    const messagesText = session.messages
      .map(msg => `**${msg.role}**: ${msg.content}`)
      .join('\n\n');

    return `### Session #${session.sessionNumber}\n\n${messagesText}`;
  }).join('\n\n---\n\n');
}

// ============================================================================
// Structured Logging Functions
// ============================================================================

interface BatchMetadata {
  batchIndex: number;
  totalBatches: number;
  sessionCount: number;
  sessionIds: string[];
  isFirstBatch: boolean;
  estimatedInputTokens: number;
}

interface ExperimentMetadata {
  experimentId: string;
  timestamp: string;
  slug: string;
  modelName: string;
  promptVersion: string;
  totalBatches: number;
  temperature: number;
  mode: 'sequential' | 'parallel';
  memo?: string;
}

/**
 * Create experiment directory for batch processing
 * Structure:
 *   logs/{experimentId}/
 *     metadata.json           - Overall experiment metadata
 *     batch-1/
 *       metadata.json         - Batch-specific metadata
 *       input-prompt.txt      - Prompt for this batch
 *       input-sessions.json   - Session data for this batch
 *       output-raw.md         - Raw LLM output
 *       output-with-meta.md   - Output with metadata header
 *     batch-2/
 *       ...
 *     final-report.md         - Final merged report
 */
function createExperimentDirectory(experimentId: string): string {
  const logsDir = path.join(process.cwd(), 'logs');
  const experimentDir = path.join(logsDir, experimentId);

  if (!fs.existsSync(logsDir)) {
    fs.mkdirSync(logsDir, { recursive: true });
  }
  if (!fs.existsSync(experimentDir)) {
    fs.mkdirSync(experimentDir, { recursive: true });
  }

  return experimentDir;
}

function createBatchDirectory(experimentDir: string, batchIndex: number): string {
  const batchDir = path.join(experimentDir, `batch-${batchIndex + 1}`);
  if (!fs.existsSync(batchDir)) {
    fs.mkdirSync(batchDir, { recursive: true });
  }
  return batchDir;
}

function saveExperimentMetadata(experimentDir: string, metadata: ExperimentMetadata) {
  const metadataPath = path.join(experimentDir, 'metadata.json');
  fs.writeFileSync(metadataPath, JSON.stringify(metadata, null, 2), 'utf-8');
}

function saveBatchMetadata(batchDir: string, metadata: BatchMetadata, usage?: any) {
  const metadataPath = path.join(batchDir, 'metadata.json');
  const metadataWithUsage = {
    ...metadata,
    usage: usage || null,
  };
  fs.writeFileSync(metadataPath, JSON.stringify(metadataWithUsage, null, 2), 'utf-8');
}

function saveBatchInputs(batchDir: string, prompt: string, sessionsData: SessionData[]) {
  const promptPath = path.join(batchDir, 'input-prompt.txt');
  const sessionsPath = path.join(batchDir, 'input-sessions.json');

  fs.writeFileSync(promptPath, prompt, 'utf-8');
  fs.writeFileSync(sessionsPath, JSON.stringify(sessionsData, null, 2), 'utf-8');
}

function saveBatchOutputs(batchDir: string, rawOutput: string, metadata: BatchMetadata, usage?: any) {
  const rawPath = path.join(batchDir, 'output-raw.md');
  const metaPath = path.join(batchDir, 'output-with-meta.md');

  // Save raw output
  fs.writeFileSync(rawPath, rawOutput, 'utf-8');

  // Save output with metadata header
  const currentDateTime = new Date().toLocaleString('ja-JP');
  const outputWithMeta = `---
Generated: ${currentDateTime}
Batch: ${metadata.batchIndex + 1}/${metadata.totalBatches}
IsFirstBatch: ${metadata.isFirstBatch}
SessionCount: ${metadata.sessionCount}
EstimatedInputTokens: ${metadata.estimatedInputTokens}
ActualInputTokens: ${usage?.promptTokens || 'N/A'}
OutputTokens: ${usage?.completionTokens || 'N/A'}
TotalTokens: ${usage?.totalTokens || 'N/A'}
---

${rawOutput}
`;

  fs.writeFileSync(metaPath, outputWithMeta, 'utf-8');
}

function saveFinalReport(experimentDir: string, report: string, experimentId: string) {
  const finalPath = path.join(experimentDir, 'final-report.md');
  const currentDateTime = new Date().toLocaleString('ja-JP');

  const reportWithMeta = `---
Generated: ${currentDateTime}
ExperimentId: ${experimentId}
Type: Batch-processed aggregate report
---

${report}
`;

  fs.writeFileSync(finalPath, reportWithMeta, 'utf-8');
}

// ============================================================================
// Main Function
// ============================================================================

async function main() {
  const startTime = Date.now();

  // Parse command line arguments
  const args = process.argv.slice(2);
  let slug: string | null = null;
  let memo: string | undefined = undefined;
  let mode: 'sequential' | 'parallel' = 'sequential';

  for (const arg of args) {
    if (arg.startsWith('--slug=')) {
      slug = arg.substring('--slug='.length);
    } else if (arg.startsWith('--memo=')) {
      memo = arg.substring('--memo='.length);
    } else if (arg.startsWith('--mode=')) {
      const modeValue = arg.substring('--mode='.length);
      if (modeValue === 'sequential' || modeValue === 'parallel') {
        mode = modeValue;
      } else {
        console.error(`❌ Error: Invalid mode "${modeValue}". Must be "sequential" or "parallel"\n`);
        process.exit(1);
      }
    }
  }

  if (!slug) {
    console.error('❌ Error: --slug parameter is required\n');
    console.log('Usage: npx tsx scripts/20251123_generate-aggregate-report-v2.ts --slug=<slug> [--mode=sequential|parallel] [--memo="memo"]\n');
    console.log('Modes:');
    console.log('  sequential (default) - Process batches one by one, incrementally updating the report');
    console.log('  parallel             - Process all batches in parallel, then merge results (faster)\n');
    console.log('Examples:');
    console.log('  npx tsx scripts/20251123_generate-aggregate-report-v2.ts --slug=bill-of-lading');
    console.log('  npx tsx scripts/20251123_generate-aggregate-report-v2.ts --slug=bill-of-lading --mode=parallel --memo="並列処理テスト"\n');
    process.exit(1);
  }

  console.log('🚀 Starting aggregate report generation...\n');
  console.log('📋 Configuration:');
  console.log(`   Slug: ${slug}`);
  console.log(`   Mode: ${mode === 'parallel' ? 'Parallel (all batches at once)' : 'Sequential (incremental)'}`);
  console.log(`   Model: ${MODEL_NAME}`);
  console.log(`   Tokens per batch: ${TOKENS_PER_BATCH.toLocaleString()}`);
  console.log(`   Max output tokens: ${MAX_OUTPUT_TOKENS.toLocaleString()}`);
  if (memo) {
    console.log(`   Memo: ${memo}`);
  }
  console.log();

  // Database connection setup
  const connectionString = process.env.POSTGRES_URL_NON_POOLING || process.env.POSTGRES_URL;
  if (!connectionString) {
    console.error('❌ Error: POSTGRES_URL or POSTGRES_URL_NON_POOLING not found in .env.vercel');
    process.exit(1);
  }

  const apiKey = process.env.AI_GATEWAY_API_KEY;
  if (!apiKey) {
    console.error('❌ Error: AI_GATEWAY_API_KEY not found in .env.vercel');
    process.exit(1);
  }

  const isLocalSupabase = connectionString?.includes('localhost') || connectionString?.includes('127.0.0.1');
  const sslConfig = isLocalSupabase ? false : (connectionString ? { rejectUnauthorized: false } : false);

  const pool = new Pool({
    connectionString: connectionString?.replace(/[?&]sslmode=[^&]*/g, ''),
    ssl: sslConfig
  });

  // Add error handler to prevent unhandled error events
  pool.on('error', (err) => {
    console.error('⚠️  Pool error (ignored):', err.message);
  });

  try {
    console.log('🔌 Connecting to production database...');

    // Get interview config
    const configResult = await pool.query(`
      SELECT title, description, landing_page, questions, knowledge_source_text FROM interview_configs WHERE slug = $1 LIMIT 1
    `, [slug]);
    console.log(`   Config query completed: ${configResult.rows.length} rows`);

    if (configResult.rows.length === 0) {
      throw new Error(`Interview config not found for slug: ${slug}`);
    }

    const interviewTitle = configResult.rows[0].title;
    const interviewDescription = configResult.rows[0].description || '';
    const landingPage = configResult.rows[0].landing_page || {};
    const questions = configResult.rows[0].questions || [];
    const knowledgeSourceText = configResult.rows[0].knowledge_source_text || '';

    // Extract data from landing_page
    const interviewOverview = landingPage.overview || '（概要なし）';
    const interviewThemes = (landingPage.themes || [])
      .map((theme: string, idx: number) => `${idx + 1}. ${theme}`)
      .join('\n') || '（テーマなし）';

    const interviewQuestions = (questions || [])
      .map((q: any, idx: number) => {
        const topic = q.topic || '（トピックなし）';
        const mainQuestion = q.mainQuestion || '';
        return `${idx + 1}. **${topic}**: ${mainQuestion}`;
      })
      .join('\n') || '（質問なし）';

    const knowledgeContext = knowledgeSourceText || '（参考知識なし）';

    console.log(`   Interview: ${interviewTitle}\n`);

    // Get all sessions for this interview (sorted by message count DESC)
    const allSessionsResult = await pool.query(`
      SELECT
        s.id,
        s.session_number,
        COUNT(m.id) as message_count
      FROM interview_sessions s
      LEFT JOIN messages m ON s.id = m.session_id
      WHERE s.slug = $1
      GROUP BY s.id, s.session_number
      HAVING COUNT(m.id) >= 7
      ORDER BY COUNT(m.id) DESC
    `, [slug]);

    const allSessionIds = allSessionsResult.rows.map(row => row.id);
    const allMessageCounts = new Map(allSessionsResult.rows.map(row => [row.id, row.message_count]));

    console.log(`📊 Total sessions available: ${allSessionIds.length}\n`);

    if (allSessionIds.length === 0) {
      console.error('❌ No sessions found with minimum 7 messages');
      process.exit(1);
    }

    // Split sessions into batches
    const batches: string[][] = [];
    let currentBatch: string[] = [];
    let currentTokens = ESTIMATED_PROMPT_OVERHEAD;

    for (const sessionId of allSessionIds) {
      const messageCount = allMessageCounts.get(sessionId) || 0;
      const estimatedSessionTokens = messageCount * 350; // Rough estimate per message

      if (currentTokens + estimatedSessionTokens > TOKENS_PER_BATCH && currentBatch.length > 0) {
        // Start new batch
        batches.push(currentBatch);
        currentBatch = [sessionId];
        currentTokens = ESTIMATED_PROMPT_OVERHEAD + estimatedSessionTokens;
      } else {
        currentBatch.push(sessionId);
        currentTokens += estimatedSessionTokens;
      }
    }

    if (currentBatch.length > 0) {
      batches.push(currentBatch);
    }

    console.log(`📦 Split into ${batches.length} batches:\n`);
    batches.forEach((batch, index) => {
      console.log(`   Batch ${index + 1}: ${batch.length} sessions`);
    });
    console.log();

    // Create experiment directory
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-').substring(0, 19);
    const experimentId = `${slug}-${PROMPT_VERSION}-${timestamp}`;

    const experimentMetadata: ExperimentMetadata = {
      experimentId,
      timestamp: new Date().toISOString(),
      slug,
      modelName: MODEL_NAME,
      promptVersion: PROMPT_VERSION,
      totalBatches: batches.length,
      temperature: 0.3,
      mode,
      ...(memo && { memo }),
    };

    console.log('📁 Creating experiment directory...');
    const experimentDir = createExperimentDirectory(experimentId);
    saveExperimentMetadata(experimentDir, experimentMetadata);
    console.log(`   ${experimentDir}\n`);

    // API key
    const apiKey = process.env.AI_GATEWAY_API_KEY;
    if (!apiKey) {
      throw new Error('AI_GATEWAY_API_KEY not found in environment');
    }

    const gateway = createGateway({ apiKey });

    // Close initial connection
    await pool.end();

    let currentReport: string = '';

    // Choose processing mode
    if (mode === 'parallel') {
      // Parallel mode: process all batches simultaneously, then merge
      currentReport = await processParallelMode(
        batches,
        experimentDir,
        gateway,
        slug,
        interviewTitle,
        interviewDescription,
        interviewOverview,
        interviewThemes,
        interviewQuestions,
        knowledgeContext,
        connectionString,
        sslConfig
      );
    } else {
      // Sequential mode: process batches one by one (original behavior)
      currentReport = await processSequentialMode(
        batches,
        experimentDir,
        gateway,
        slug,
        interviewTitle,
        interviewDescription,
        interviewOverview,
        interviewThemes,
        interviewQuestions,
        knowledgeContext,
        connectionString,
        sslConfig
      );
    }

    // Save final report to experiment directory
    console.log('\n📝 Saving final report to experiment directory...');
    saveFinalReport(experimentDir, currentReport, experimentId);
    console.log(`   ✓ final-report.md\n`);

    // Also save to backups directory for backward compatibility
    const finalTimestamp = new Date().toISOString().replace(/[:.]/g, '-').substring(0, 19);
    const backupsDir = path.join(process.cwd(), 'backups');

    if (!fs.existsSync(backupsDir)) {
      fs.mkdirSync(backupsDir, { recursive: true });
    }

    const outputPath = path.join(backupsDir, `aggregate-report-v2-${slug}-${finalTimestamp}.md`);

    // Add metadata
    const currentDateTime = new Date().toLocaleString('ja-JP');
    const totalSessions = allSessionIds.length;
    const reportWithMetadata = `---
Generated: ${currentDateTime}
Model: ${MODEL_NAME}
Slug: ${slug}
SessionCount: ${totalSessions}
Method: ${mode === 'parallel' ? 'Parallel' : 'Incremental'} (${batches.length} batches)
PromptVersion: ${PROMPT_VERSION}
ExperimentId: ${experimentId}
---

${currentReport}
`;

    fs.writeFileSync(outputPath, reportWithMetadata, 'utf-8');

    console.log('✅ Final report generated!\n');
    console.log('📊 Statistics:');
    console.log(`   Total sessions: ${totalSessions}`);
    console.log(`   Batches processed: ${batches.length}`);
    console.log(`   Final output size: ${(reportWithMetadata.length / 1024).toFixed(2)} KB`);
    console.log(`   Processing time: ${((Date.now() - startTime) / 1000).toFixed(2)}s\n`);
    console.log('📁 Results saved:');
    console.log(`   Experiment: logs/${experimentId}/`);
    console.log(`   Backup: ${outputPath}\n`);
    console.log('✨ Done!\n');

  } catch (error) {
    console.error('❌ Error:', error);
    throw error;
  }
}

// ============================================================================
// Sequential Mode (original implementation)
// ============================================================================

async function processSequentialMode(
  batches: string[][],
  experimentDir: string,
  gateway: any,
  slug: string,
  interviewTitle: string,
  interviewDescription: string,
  interviewOverview: string,
  interviewThemes: string,
  interviewQuestions: string,
  knowledgeContext: string,
  connectionString: string | undefined,
  sslConfig: any
): Promise<string> {
  let currentReport: string = '';

  // Process each batch
  for (let batchIndex = 0; batchIndex < batches.length; batchIndex++) {
      const batch = batches[batchIndex];
      const isFirstBatch = batchIndex === 0;

      console.log(`\n${'='.repeat(60)}`);
      console.log(`📦 Processing Batch ${batchIndex + 1}/${batches.length}`);
      console.log(`${'='.repeat(60)}\n`);

      // Create new pool for this batch
      const batchPool = new Pool({
        connectionString: connectionString?.replace(/[?&]sslmode=[^&]*/g, ''),
        ssl: sslConfig
      });

      // Add error handler to prevent unhandled error events
      batchPool.on('error', (err) => {
        console.error('⚠️  Batch pool error (ignored):', err.message);
      });

      // Fetch session data for this batch
      const sessionsData = await fetchSessionData(batchPool, slug, batch);
      const sessionsText = formatSessionsData(sessionsData);

      // Close connection before LLM call (to avoid timeout during long LLM processing)
      await batchPool.end();

      // Prepare prompt
      let prompt: string;
      const outputLengthGuidance = 'Target output length: 10,000-20,000 characters per batch. Provide detailed analysis with extensive quotations.';

      if (isFirstBatch) {
        // Initial report generation
        console.log('🤖 Generating initial report...\n');
        prompt = INITIAL_PROMPT_TEMPLATE
          .replace(/\{\{interviewTitle\}\}/g, interviewTitle)
          .replace(/\{\{interviewDescription\}\}/g, interviewDescription)
          .replace(/\{\{interviewOverview\}\}/g, interviewOverview)
          .replace(/\{\{interviewThemes\}\}/g, interviewThemes)
          .replace(/\{\{interviewQuestions\}\}/g, interviewQuestions)
          .replace(/\{\{knowledgeContext\}\}/g, knowledgeContext)
          .replace(/\{\{sessionCount\}\}/g, String(sessionsData.length))
          .replace(/\{\{sessionsData\}\}/g, sessionsText)
          .replace(/\{\{outputLengthGuidance\}\}/g, outputLengthGuidance);
      } else {
        // Incremental update
        console.log(`🔄 Updating report with new sessions...\n`);
        prompt = UPDATE_PROMPT_TEMPLATE
          .replace(/\{\{interviewTitle\}\}/g, interviewTitle)
          .replace(/\{\{interviewDescription\}\}/g, interviewDescription)
          .replace(/\{\{interviewOverview\}\}/g, interviewOverview)
          .replace(/\{\{interviewThemes\}\}/g, interviewThemes)
          .replace(/\{\{interviewQuestions\}\}/g, interviewQuestions)
          .replace(/\{\{knowledgeContext\}\}/g, knowledgeContext)
          .replace(/\{\{previousReport\}\}/g, currentReport)
          .replace(/\{\{newSessionCount\}\}/g, String(sessionsData.length))
          .replace(/\{\{sessionsData\}\}/g, sessionsText)
          .replace(/\{\{outputLengthGuidance\}\}/g, outputLengthGuidance);
      }

      const estimatedInputTokens = estimateTokens(prompt);
      console.log(`   Input tokens (estimated): ${estimatedInputTokens.toLocaleString()}`);
      console.log(`   Sessions in batch: ${sessionsData.length}`);

      // Create batch directory and save inputs
      console.log('   📁 Creating batch directory...');
      const batchDir = createBatchDirectory(experimentDir, batchIndex);

      const batchMetadata: BatchMetadata = {
        batchIndex,
        totalBatches: batches.length,
        sessionCount: sessionsData.length,
        sessionIds: batch,
        isFirstBatch,
        estimatedInputTokens,
      };

      saveBatchInputs(batchDir, prompt, sessionsData);
      console.log(`   💾 Saved: input-prompt.txt, input-sessions.json`);

      console.log(`   🤖 Calling Gemini 3.0 Pro...\n`);

      // Call LLM
      const result = await generateText({
        model: gateway(MODEL_NAME),
        prompt,
        temperature: 0.3,
        maxRetries: 0,
        abortSignal: AbortSignal.timeout(600000), // 10 minutes
      });

      currentReport = result.text;

      // Save batch outputs
      saveBatchOutputs(batchDir, currentReport, batchMetadata, result.usage);
      saveBatchMetadata(batchDir, batchMetadata, result.usage);
      console.log(`   💾 Saved: output-raw.md, output-with-meta.md, metadata.json`);

      console.log(`✅ Batch ${batchIndex + 1} completed!`);
      if (result.usage) {
        const usage = result.usage as any;
        console.log(`   Output tokens: ${usage.completionTokens?.toLocaleString() || 'N/A'}`);
        console.log(`   Total tokens: ${usage.totalTokens?.toLocaleString() || 'N/A'}`);
      }
      console.log(`   Output size: ${(currentReport.length / 1024).toFixed(2)} KB`);
    }

    return currentReport;
}

// ============================================================================
// Parallel Mode (concurrent batch processing with final merge)
// ============================================================================

async function processParallelMode(
  batches: string[][],
  experimentDir: string,
  gateway: any,
  slug: string,
  interviewTitle: string,
  interviewDescription: string,
  interviewOverview: string,
  interviewThemes: string,
  interviewQuestions: string,
  knowledgeContext: string,
  connectionString: string | undefined,
  sslConfig: any
): Promise<string> {
  console.log('🚀 Processing all batches in parallel...\n');

  // Process all batches concurrently
  const batchPromises = batches.map(async (batch, batchIndex) => {
    console.log(`\n${'='.repeat(60)}`);
    console.log(`📦 Starting Batch ${batchIndex + 1}/${batches.length} (parallel)`);
    console.log(`${'='.repeat(60)}\n`);

    // Create new pool for this batch
    const batchPool = new Pool({
      connectionString: connectionString?.replace(/[?&]sslmode=[^&]*/g, ''),
      ssl: sslConfig
    });

    // Add error handler
    batchPool.on('error', (err) => {
      console.error(`⚠️  Batch ${batchIndex + 1} pool error (ignored):`, err.message);
    });

    // Fetch session data for this batch
    const sessionsData = await fetchSessionData(batchPool, slug, batch);
    const sessionsText = formatSessionsData(sessionsData);

    // Close connection before LLM call
    await batchPool.end();

    // Prepare prompt (always use INITIAL template for parallel mode)
    const outputLengthGuidance = 'Target output length: 10,000-20,000 characters per batch. Provide detailed analysis with extensive quotations.';

    console.log(`   🤖 [Batch ${batchIndex + 1}] Generating report in parallel...\n`);
    const prompt = INITIAL_PROMPT_TEMPLATE
      .replace(/\{\{interviewTitle\}\}/g, interviewTitle)
      .replace(/\{\{interviewDescription\}\}/g, interviewDescription)
      .replace(/\{\{interviewOverview\}\}/g, interviewOverview)
      .replace(/\{\{interviewThemes\}\}/g, interviewThemes)
      .replace(/\{\{interviewQuestions\}\}/g, interviewQuestions)
      .replace(/\{\{knowledgeContext\}\}/g, knowledgeContext)
      .replace(/\{\{sessionCount\}\}/g, String(sessionsData.length))
      .replace(/\{\{sessionsData\}\}/g, sessionsText)
      .replace(/\{\{outputLengthGuidance\}\}/g, outputLengthGuidance);

    const estimatedInputTokens = estimateTokens(prompt);
    console.log(`   [Batch ${batchIndex + 1}] Input tokens (estimated): ${estimatedInputTokens.toLocaleString()}`);
    console.log(`   [Batch ${batchIndex + 1}] Sessions in batch: ${sessionsData.length}`);

    // Create batch directory and save inputs
    console.log(`   [Batch ${batchIndex + 1}] 📁 Creating batch directory...`);
    const batchDir = createBatchDirectory(experimentDir, batchIndex);

    const batchMetadata: BatchMetadata = {
      batchIndex,
      totalBatches: batches.length,
      sessionCount: sessionsData.length,
      sessionIds: batch,
      isFirstBatch: batchIndex === 0,
      estimatedInputTokens,
    };

    saveBatchInputs(batchDir, prompt, sessionsData);
    console.log(`   [Batch ${batchIndex + 1}] 💾 Saved: input-prompt.txt, input-sessions.json`);

    console.log(`   [Batch ${batchIndex + 1}] 🤖 Calling Gemini 3.0 Pro...\n`);

    // Call LLM
    const result = await generateText({
      model: gateway(MODEL_NAME),
      prompt,
      temperature: 0.3,
      maxRetries: 0,
      abortSignal: AbortSignal.timeout(600000), // 10 minutes
    });

    const batchReport = result.text;

    // Save batch outputs
    saveBatchOutputs(batchDir, batchReport, batchMetadata, result.usage);
    saveBatchMetadata(batchDir, batchMetadata, result.usage);
    console.log(`   [Batch ${batchIndex + 1}] 💾 Saved: output-raw.md, output-with-meta.md, metadata.json`);

    console.log(`✅ Batch ${batchIndex + 1} completed!`);
    if (result.usage) {
      const usage = result.usage as any;
      console.log(`   [Batch ${batchIndex + 1}] Output tokens: ${usage.completionTokens?.toLocaleString() || 'N/A'}`);
      console.log(`   [Batch ${batchIndex + 1}] Total tokens: ${usage.totalTokens?.toLocaleString() || 'N/A'}`);
    }
    console.log(`   [Batch ${batchIndex + 1}] Output size: ${(batchReport.length / 1024).toFixed(2)} KB`);

    return batchReport;
  });

  // Wait for all batches to complete
  console.log('\n⏳ Waiting for all parallel batches to complete...\n');
  const batchReports = await Promise.all(batchPromises);
  console.log('✅ All batches completed!\n');

  // Merge all batch reports using MERGE_PROMPT
  console.log(`\n${'='.repeat(60)}`);
  console.log(`🔀 Merging ${batchReports.length} batch reports...`);
  console.log(`${'='.repeat(60)}\n`);

  const combinedBatchReports = batchReports
    .map((report, idx) => `## バッチ ${idx + 1} の分析結果\n\n${report}`)
    .join('\n\n' + '='.repeat(60) + '\n\n');

  const mergeOutputLengthGuidance = 'Target output length: Comprehensive report with all information from batch reports preserved. Length may exceed individual batch reports to ensure no information is lost.';

  const mergePrompt = MERGE_PROMPT_TEMPLATE
    .replace(/\{\{interviewTitle\}\}/g, interviewTitle)
    .replace(/\{\{interviewDescription\}\}/g, interviewDescription)
    .replace(/\{\{interviewOverview\}\}/g, interviewOverview)
    .replace(/\{\{interviewThemes\}\}/g, interviewThemes)
    .replace(/\{\{interviewQuestions\}\}/g, interviewQuestions)
    .replace(/\{\{knowledgeContext\}\}/g, knowledgeContext)
    .replace(/\{\{batchCount\}\}/g, String(batchReports.length))
    .replace(/\{\{batchReports\}\}/g, combinedBatchReports)
    .replace(/\{\{outputLengthGuidance\}\}/g, mergeOutputLengthGuidance);

  const estimatedMergeTokens = estimateTokens(mergePrompt);
  console.log(`   Merge input tokens (estimated): ${estimatedMergeTokens.toLocaleString()}`);
  console.log(`   🤖 Calling Gemini 3.0 Pro for merge...\n`);

  // Call LLM for merge
  const mergeResult = await generateText({
    model: gateway(MODEL_NAME),
    prompt: mergePrompt,
    temperature: 0.3,
    maxRetries: 0,
    abortSignal: AbortSignal.timeout(600000), // 10 minutes
  });

  const finalReport = mergeResult.text;

  console.log(`✅ Merge completed!`);
  if (mergeResult.usage) {
    const usage = mergeResult.usage as any;
    console.log(`   Output tokens: ${usage.completionTokens?.toLocaleString() || 'N/A'}`);
    console.log(`   Total tokens: ${usage.totalTokens?.toLocaleString() || 'N/A'}`);
  }
  console.log(`   Output size: ${(finalReport.length / 1024).toFixed(2)} KB`);

  // Save merge artifacts
  const mergeDir = path.join(experimentDir, 'merge');
  if (!fs.existsSync(mergeDir)) {
    fs.mkdirSync(mergeDir, { recursive: true });
  }

  fs.writeFileSync(path.join(mergeDir, 'input-prompt.txt'), mergePrompt, 'utf-8');
  fs.writeFileSync(path.join(mergeDir, 'output-raw.md'), finalReport, 'utf-8');

  const mergeMetadata = {
    batchCount: batchReports.length,
    estimatedInputTokens: estimatedMergeTokens,
    usage: mergeResult.usage
  };
  fs.writeFileSync(path.join(mergeDir, 'metadata.json'), JSON.stringify(mergeMetadata, null, 2), 'utf-8');

  console.log(`   💾 Saved merge artifacts to: merge/\n`);

  return finalReport;
}

main().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});
