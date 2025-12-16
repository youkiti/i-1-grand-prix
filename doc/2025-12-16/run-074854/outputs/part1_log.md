# Part 1 Outputs (Individual Document Analysis)

## File: metadata_shugiin.go.jp_20251213_064119.json

提供されたドキュメント（`metadata_shugiin.go.jp_20251213_064119.json`）は、衆議院選挙制度に関する協議会や調査会のメタデータ（ファイル名、URL、ダウンロード日時など）のみを含んでおり、**実際のPDFファイルの内容（議論の本文）は含まれていません**。

したがって、このメタデータのみから「議員定数削減」に関する具体的な論点、課題、懸念点を抽出することは不可能です。

**結論として、現時点では法案に盛り込むべき論点を抽出することはできません。**

もし、これらのPDFファイルの内容（テキストデータ）が提供されれば、目的（議員定数削減に関連する論点の抽出）に従って分析し、YAML形式で出力いたします。

```yaml
topics: []
evidence_chunks: []
```

---

## File: senkyoseido_01gijigaiyo.pdf

このドキュメント（senkyoseido_01gijigaiyo.pdf）は、「衆議院選挙制度に関する調査会」の第1回議事概要であり、今後の調査会のスケジュールと検討事項が示されています。

この資料から「議員定数削減問題」に直接関連する論点として抽出できるのは、調査会がこの問題を検討事項の一つとしてスケジュールに組み込んでいるという事実のみです。具体的な削減の是非や方法に関する議論内容は含まれていません。

以下に、抽出した論点をYAML形式で示します。

```yaml
topics:
  - id: "topic_001"
    title: "議員定数削減問題の調査会における検討事項としての位置づけ"
    category: "主要論点"
    summary: "衆議院選挙制度に関する調査会において、「各党が選挙の際に公約した『定数削減問題』について検討を行う」ことが、今後の主要な検討事項の一つとして正式にスケジュールに組み込まれた。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_01gijigaiyo"
        source_filename: "senkyoseido_01gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01gijigaiyo.pdf/$File/senkyoseido_01gijigaiyo.pdf"
        source_date: "平成26年９月11日"
        verbatim_quote: |
           次に、各党が選挙の際に公約した「定数削減問題」について検討を
          行う。
        position: null
        speaker: null
        context: "今後の調査会の検討スケジュールに関する決定事項"
```

---

## File: senkyoseido_01shiryo1.pdf

提供されたドキュメント（`senkyoseido_01shiryo1.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**「議員定数削減」そのものに関する具体的な論点、課題、懸念、あるいは新たなアイデアは一切含まれていません**。

このドキュメントは、調査会の設置根拠、委員の選任、会議の運営方法、事務局の担当、答申の時期に関する事務的な規定のみを定めています。

したがって、「議員定数削減」に直接関連する論点を抽出することはできません。

```yaml
topics:
  - id: "topic_001"
    title: "議員定数削減に関する具体的な論点の欠如"
    category: "課題・懸念"
    summary: "提供されたドキュメントは、衆議院選挙制度に関する調査会の運営細則（案）であり、議員定数削減の具体的な方法論、削減の是非、削減に伴う影響など、法案作成に資する論点は一切含まれていない。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_01shiryo1"
        source_filename: "senkyoseido_01shiryo1.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
        source_date: "平成２６年６月１９日"
        verbatim_quote: |
          １ 衆議院議院運営委員会での議決（平成２６年６月１９日）に基づき、衆議院選挙制度に関
          する調査・検討等を行うため、議長のもとに「衆議院選挙制度に関する調査会（以下「調
          査会」という。 ） 」を置く。
        position: null
        speaker: null
        context: "調査会の設置根拠と目的の記述。具体的な検討事項（定数削減など）の言及はない。"
      - id: "chunk_002"
        source_doc_id: "senkyoseido_01shiryo1"
        source_filename: "senkyoseido_01shiryo1.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
        source_date: null
        verbatim_quote: |
          ９ 議長への答申は、現議員の任期を念頭に、立法作業や周知期間を考慮して行う。
        position: null
        speaker: null
        context: "答申の時期に関する規定。定数削減の是非や方法に関する議論ではない。"
```

---

## File: senkyoseido_01shiryo1_1.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_1.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**「議員定数削減」そのものに関する具体的な議論や論点、課題、懸念点は一切含まれていません**。

このドキュメントは、調査会の設置根拠、委員の選任、会議の運営方法、事務局の担当など、**事務的な手続き**に関する規定のみを定めています。

したがって、「議員定数削減」に直接関係する論点を抽出することはできません。

```yaml
topics: []
```

---

## File: senkyoseido_01shiryo1_10.pdf

このドキュメント（`senkyoseido_01shiryo1_10.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）であり、**調査会の設置目的や運営方法**について定めています。

**「議員定数削減」**そのものに関する具体的な論点、課題、あるいは削減案に関する議論は、この運営細則の中には**一切含まれていません**。

運営細則の第9項に「現議員の任期を念頭に、立法作業や周知期間を考慮して行う」という記述がありますが、これは調査会の「答申」の時期に関するものであり、**定数削減の是非や方法論**に関する論点ではありません。

したがって、**「議員定数削減」に直接関係する論点は、このドキュメントからは抽出できません**。

```yaml
topics:
  - id: "topic_001"
    title: "議員定数削減に関する具体的な論点の欠如"
    category: "課題・懸念"
    summary: "本資料は衆議院選挙制度に関する調査会の運営細則であり、調査会の設置目的や会議運営に関する事務的な事項を定めている。議員定数削減の具体的な方法論、削減の是非、削減に伴う影響など、法案作成に資する具体的な論点は一切含まれていない。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_01shiryo1_10.pdf"
        source_filename: "senkyoseido_01shiryo1_10.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
        source_date: "平成２６年６月１９日"
        verbatim_quote: |
          １ 衆議院議院運営委員会での議決（平成２６年６月１９日）に基づき、衆議院選挙制度に関する調査・検討等を行うため、議長のもとに「衆議院選挙制度に関する調査会（以下「調査会」という。 ） 」を置く。
        position: null
        speaker: null
        context: "調査会の設置根拠と目的の記述。"
      - id: "chunk_002"
        source_doc_id: "senkyoseido_01shiryo1_10.pdf"
        source_filename: "senkyoseido_01shiryo1_10.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
        source_date: "平成２６年６月１９日"
        verbatim_quote: |
          ９ 議長への答申は、現議員の任期を念頭に、立法作業や周知期間を考慮して行う。
        position: null
        speaker: null
        context: "答申の時期に関する規定であり、定数削減の具体的な議論ではない。"
```

---

## File: senkyoseido_01shiryo1_11.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_11.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**「議員定数削減」そのものに関する具体的な論点、課題、懸念、またはアイデアは一切含まれていません**。

このドキュメントは、調査会の設置根拠、委員の選任、会議の運営、事務局、答申時期など、**調査会を運営するための事務的なルール**を定めたものです。

したがって、「議員定数削減」に直接関係する論点を抽出することはできません。

```yaml
topics:
  - id: "topic_001"
    title: "議員定数削減に関する具体的な論点の欠如"
    category: "課題・懸念"
    summary: "提供されたドキュメントは、衆議院選挙制度に関する調査会の運営細則であり、議員定数削減の具体的な是非、方法論、影響に関する議論や論点は一切含まれていない。今後の法案作成に向けた論点抽出には不十分である。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_01shiryo1_11"
        source_filename: "senkyoseido_01shiryo1_11.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
        source_date: "平成２６年６月１９日"
        verbatim_quote: |
          １ 衆議院議院運営委員会での議決（平成２６年６月１９日）に基づき、衆議院選挙制度に関
          する調査・検討等を行うため、議長のもとに「衆議院選挙制度に関する調査会（以下「調
          査会」という。 ） 」を置く。
        position: null
        speaker: null
        context: "調査会の設置根拠を示す部分であり、調査の対象が選挙制度全般であることが示唆されるが、定数削減に特化した記述はない。"
```

---

## File: senkyoseido_01shiryo1_12.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_12.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**議員定数削減**そのものに関する具体的な議論や論点、課題、懸念点、アイデアは一切含まれていません。

このドキュメントは、調査会の設置根拠、委員の選任、会議の運営方法、事務体制、答申時期に関する事務的な規定のみを定めています。

したがって、「議員定数削減」に直接関連する論点を抽出することはできません。

```yaml
topics: []
evidence_chunks: []
```

---

## File: senkyoseido_01shiryo1_13.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_13.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）であり、調査会の設置目的、委員構成、会議運営に関する事務的なルールを定めたものです。

このドキュメントには、**「議員定数削減」そのものの具体的な論点、課題、懸念点、あるいは新たなアイデアは一切含まれていません**。

ドキュメントの目的は「衆議院選挙制度に関する調査・検討等を行うため」の調査会を設置することであり、その設置根拠（p.1の1項）はありますが、**調査会が何を議論すべきか（＝議員定数削減の論点）については触れられていません**。

したがって、**「議員定数削減」に直接関係する論点の抽出は不可能**です。

以下に、この制約に基づき、YAMLスキーマに従って空の（または、調査会設置という最も間接的な論点のみを含む）構造を出力します。ただし、指示の「最重要フィルタ: 『議員定数削減』に直接関係のない内容はすべて除外」に従うと、出力すべき論点は存在しないことになります。

**指示の厳密な適用に基づき、抽出できる論点がないため、空の配列を出力します。**

```yaml
topics: []
```

---

## File: senkyoseido_01shiryo1_14.pdf

ご提示いただいたドキュメント（`senkyoseido_01shiryo1_14.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**「議員定数削減」そのものの具体的な論点、課題、あるいは設計に関する記述は一切含まれていません**。

このドキュメントは、調査会を設置し、その運営方法（委員の選任、会議の公開性、事務局の担当など）を定めた規則案です。

したがって、「議員定数削減」に直接関連する論点を抽出するという目的に対して、この資料から抽出できる具体的な論点は存在しません。

ただし、将来的な法案作成に向けた「前提」として、調査会の**答申時期**に関する記述は、法案化のスケジュールに影響を与えるため、関連情報として抽出します。

```yaml
topics:
  - id: "topic_001"
    title: "調査会の答申時期と法案化への影響"
    category: "その他"
    summary: "調査会が議長へ答申する時期について、現議員の任期、立法作業期間、周知期間を考慮する必要があることが示されており、これが議員定数削減の実現スケジュールに制約を与える。"
    
    spectrum: null

evidence_chunks:
  - id: "chunk_001"
    source_doc_id: "senkyoseido_01shiryo1_14.pdf"
    source_filename: "senkyoseido_01shiryo1_14.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
    source_date: "平成２６年６月１９日"
    verbatim_quote: |
      ９ 議長への答申は、現議員の任期を念頭に、立法作業や周知期間を考慮して行う。
    position: null
    speaker: null
    context: "調査会の運営細則における答申に関する規定。議員定数削減の議論が法案化されるまでのタイムライン設定の重要性を示唆している。"
```

---

## File: senkyoseido_01shiryo1_15.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_15.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）であり、調査会の設置目的、委員構成、会議運営に関する事務的な規定を定めたものです。

このドキュメントには、**「議員定数削減」そのものの具体的な論点、課題、懸念点、あるいは削減案に関する議論は一切含まれていません**。記載されているのは、調査会をどのように運営するかという手続き的な事項のみです。

したがって、「議員定数削減」に直接関係する論点を抽出することはできません。

以下に、指示されたフィルタ（「議員定数削減」に直接関係のない内容はすべて除外）を厳密に適用した結果、抽出された論点がないことを示すYAMLを出力します。

```yaml
topics: []
```

---

## File: senkyoseido_01shiryo1_16.pdf

ご提示いただいたドキュメント（`senkyoseido_01shiryo1_16.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**「議員定数削減」そのものに関する具体的な論点、課題、懸念、あるいは設計案についての記述は一切含まれていません**。

このドキュメントは、調査会を設置し、その運営（委員の選任、会議の公開・非公開、事務局、答申時期など）を定める規則を定めたものです。

したがって、「議員定数削減」に直接関連する論点を抽出することはできません。

以下に、ドキュメントの内容に基づき、**「議員定数削減」の検討プロセスに関する間接的な論点**として、調査会の設置と答申時期に関する情報を抽出しますが、これは「議員定数削減」の具体的な内容に関する論点ではない点にご留意ください。

```yaml
topics:
  - id: "topic_001"
    title: "調査会の答申時期の制約"
    category: "課題・懸念"
    summary: "調査会が、現議員の任期を念頭に置いて答申を行うことが定められており、これが議員定数削減の議論のペースや結論に制約を与える可能性がある。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_01shiryo1_16.pdf"
        source_filename: "senkyoseido_01shiryo1_16.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
        source_date: "平成２６年６月１９日"
        verbatim_quote: |
          ９ 議長への答申は、現議員の任期を念頭に、立法作業や周知期間を考慮して行う。
        position: null
        speaker: null
        context: "調査会の運営細則における答申に関する規定"
```

---

## File: senkyoseido_01shiryo1_17.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_17.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**「議員定数削減」そのものに関する具体的な議論、論点、課題、懸念、あるいは新たなアイデアは一切含まれていません**。

このドキュメントは、調査会を設置し、その運営方法（委員の選任、会議の公開・非公開、事務局の担当、議長への答申時期など）を定めた事務的な規則案です。

したがって、「議員定数削減」に直接関連する論点を抽出することは不可能です。

以下に、指示されたフィルタ（「議員定数削減」に直接関係のない内容はすべて除外）を厳密に適用した結果、抽出された論点がないことを示すYAMLを出力します。

```yaml
topics: []
```

---

## File: senkyoseido_01shiryo1_2.pdf

ご提示いただいたドキュメント（senkyoseido_01shiryo1_2.pdf）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関する資料であり、**「議員定数削減」そのものに関する具体的な議論や論点、課題、懸念点**は一切含まれていません。

この資料は、調査会の設置根拠、委員の選任、会議の運営、事務処理、議長への答申時期に関する事務的なルールを定めたものです。

したがって、**「議員定数削減」に直接関係する論点を抽出することはできません**。

以下に、指示されたフィルタ（「議員定数削減」に直接関係のない内容はすべて除外）を厳密に適用した結果、抽出されたトピックがないことを示すYAMLを出力します。

```yaml
topics: []
```

---

## File: senkyoseido_01shiryo1_3.pdf

ご提示いただいたドキュメント（`senkyoseido_01shiryo1_3.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）であり、**調査会の設置目的や運営方法**について定めたものです。

このドキュメントには、**「議員定数削減」そのものの具体的な議論、論点、課題、あるいは削減案に関する記述は一切含まれていません**。

したがって、**「議員定数削減」に直接関連する論点を抽出することはできません**。

以下に、抽出できなかった旨を、指定されたYAMLフォーマットで示します。

```yaml
topics:
  - id: "topic_000"
    title: "議員定数削減に関する具体的な論点の欠如"
    category: "課題・懸念"
    summary: "提供されたドキュメントは、衆議院選挙制度に関する調査会の運営細則（案）であり、調査会の設置根拠、委員構成、会議運営に関する事務的な規定のみを定めている。議員定数削減の具体的な是非、方法論、影響に関する議論や論点は一切含まれていないため、本資料からは抽出不可能である。"
    
    spectrum: null

evidence_chunks:
  - id: "chunk_001"
    source_doc_id: "senkyoseido_01shiryo1_3"
    source_filename: "senkyoseido_01shiryo1_3.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
    source_date: "平成26年6月19日"
    verbatim_quote: |
      １ 衆議院議院運営委員会での議決（平成２６年６月１９日）に基づき、衆議院選挙制度に
      関する調査・検討等を行うため、議長のもとに「衆議院選挙制度に関する調査会（以下「調
      査会」という。 ） 」を置く。
    position: null
    speaker: null
    context: "調査会の設置根拠。選挙制度全般の調査・検討を行うことが目的とされているが、定数削減に特化しているわけではない。"
  - id: "chunk_002"
    source_doc_id: "senkyoseido_01shiryo1_3"
    source_filename: "senkyoseido_01shiryo1_3.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
    source_date: null
    verbatim_quote: |
      ９ 議長への答申は、現議員の任期を念頭に、立法作業や周知期間を考慮して行う。
    position: null
    speaker: null
    context: "答申の時期に関する規定。定数削減の議論が行われる場合、任期や周知期間が考慮されるべき要素ではあるが、本資料自体には削減に関する具体的な論点は含まれていない。"
```

---

## File: senkyoseido_01shiryo1_4.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_4.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）であり、調査会の設置目的、委員構成、会議運営に関する事務的な規定を定めたものです。

このドキュメントには、**「議員定数削減」そのものの具体的な議論、論点、課題、あるいは設計に関する記述は一切含まれていません**。記載されているのは、調査会をどのように運営するかという手続き的な事項のみです。

したがって、「議員定数削減」に直接関係する論点を抽出することはできません。

```yaml
topics: []
```

---

## File: senkyoseido_01shiryo1_5.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_5.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）であり、調査会の設置目的、委員構成、会議の進め方、事務処理など、**調査会の運営に関する事務的な規定**を定めたものです。

このドキュメントには、「議員定数削減」そのものの是非、具体的な削減方法、削減に伴う影響、あるいは削減を巡る具体的な議論や論点は**一切含まれていません**。

したがって、**「議員定数削減」に直接関連する論点を抽出することはできません**。

以下に、指示されたフィルタリング基準（「議員定数削減」に直接関係のない内容はすべて除外）に基づき、抽出結果をYAML形式で示します。

```yaml
topics: []
```

---

## File: senkyoseido_01shiryo1_6.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_6.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**「議員定数削減」そのものに関する具体的な論点、課題、懸念、あるいは新たなアイデアは一切含まれていません**。

このドキュメントは、調査会の設置根拠、委員の選任、会議の運営方法、事務局、答申時期など、**事務的な手続き**に関する規定のみを定めています。

したがって、「議員定数削減」に直接関係する論点を抽出することはできません。

```yaml
topics: []
```

---

## File: senkyoseido_01shiryo1_7.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_7.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**「議員定数削減」そのものに関する具体的な議論や論点、課題、懸念点、アイデアは一切含まれていません**。

このドキュメントは、調査会の設置根拠、委員の選任、会議の運営方法、事務局、答申時期など、**事務的な手続き**に関する規定のみを定めています。

したがって、「議員定数削減」に直接関係する論点を抽出することはできません。

```yaml
topics: []
```

---

## File: senkyoseido_01shiryo1_8.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_8.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）に関するものであり、**「議員定数削減」そのものに関する具体的な議論や論点、課題、懸念事項は一切含まれていません**。

このドキュメントは、調査会の設置根拠、委員の選任、会議の運営方法、事務局、答申時期に関する事務的なルールを定めたものです。

したがって、「議員定数削減」に直接関連する論点を抽出することはできません。

```yaml
topics:
  - id: "topic_001"
    title: "議員定数削減に関する具体的な論点の欠如"
    category: "課題・懸念"
    summary: "提供されたドキュメントは、衆議院選挙制度に関する調査会の運営細則（案）であり、議員定数削減の是非、削減方法、影響など、法案作成に資する具体的な論点や議論内容を含んでいない。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_01shiryo1_8.pdf"
        source_filename: "senkyoseido_01shiryo1_8.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
        source_date: null
        verbatim_quote: |
          １ 衆議院議院運営委員会での議決（平成２６年６月１９日）に基づき、衆議院選挙制度に関する調査・検討等を行うため、議長のもとに「衆議院選挙制度に関する調査会（以下「調査会」という。 ） 」を置く。
        position: null
        speaker: null
        context: "調査会の設置根拠を示す記述。"
      - id: "chunk_002"
        source_doc_id: "senkyoseido_01shiryo1_8.pdf"
        source_filename: "senkyoseido_01shiryo1_8.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_01shiryo1.pdf/$File/senkyoseido_01shiryo1.pdf"
        source_date: null
        verbatim_quote: |
          ９ 議長への答申は、現議員の任期を念頭に、立法作業や周知期間を考慮して行う。
        position: null
        speaker: null
        context: "答申の時期に関する記述であり、具体的な削減内容に関する議論ではない。"
```

---

## File: senkyoseido_01shiryo1_9.pdf

提供されたドキュメント（`senkyoseido_01shiryo1_9.pdf`）は、「衆議院選挙制度に関する調査会」の運営細則（案）であり、調査会の設置目的、委員構成、会議運営に関する事務的なルールを定めたものです。

このドキュメントには、**「議員定数削減」そのものの具体的な論点、課題、懸念点、あるいは削減案に関する議論は一切含まれていません**。

唯一、議員定数削減の議論の「期限」に関わる記述として、答申の時期に関する記述がありますが、これは削減の「内容」に関する論点ではないため、**「議員定数削減」に直接関係する論点として抽出できるものはありません**。

したがって、目的のフィルタ（「議員定数削減」に直接関係のない内容はすべて除外）に基づき、抽出される論点はゼロとなります。

```yaml
topics: []
```

---

## File: senkyoseido_02.gijigaiyo.pdf

このドキュメント（senkyoseido_02.gijigaiyo.pdf）は、衆議院選挙制度に関する調査会（第2回）の議事概要であり、主な議題は「衆議院小選挙区の一票の較差」です。

**議員定数削減**に直接関連する具体的な議論や試算は、この資料からは**確認できません**でした。資料で言及されているのは、主に以下の点です。

1.  **定数配分方式の試算**: 現行定数295を「1人別枠方式」および「人口比例方式（最大剰余法）」で配分した場合の試算値が示されていますが、これは**定数削減の是非**ではなく、**定数配分方法の比較**に関するものです（p.3）。
2.  **1人別枠方式の存続**: 緊急是正法（0増5減）が1人別枠方式を残しているかどうかの疑問が呈されています（p.3）。
3.  **配分規定の欠如**: 緊急是正法により衆議院議員選挙区画定審議会設置法第3条第2項（1人別枠方式に係る規定）が削除された結果、総定数の各都道府県への配分規定がなくなっており、新たな規定が必要かどうかが論点となっています（p.4）。

これらの論点は、**定数配分（誰に何議席配分するか）**に関わるものであり、**総定数そのものを削減する**という論点（議員定数削減）とは直接的な関連性が薄いと判断されます。

したがって、本ドキュメントからは、**「議員定数削減」に直接関連する重要な論点、課題、懸念点は抽出できない**と結論付けます。

```yaml
topics: []
```

---

## File: senkyoseido_03.gijigaiyo.pdf

このドキュメントは「衆議院選挙制度に関する調査会」の第3回議事概要であり、主に「一票の較差」是正に関する議論が中心です。**「議員定数削減」**に直接関連する具体的な議論や提案は、この議事概要からは**確認できません**でした。

議論の焦点は、主に以下の点に絞られています。
1.  一票の較差是正（緊急是正の内容と今後の是正頻度・方法）
2.  議員定数の都道府県への配分方式（ヘア式、ドント方式などの比較）
3.  定数配分の基準となる人口統計（国勢調査人口 vs 住民基本台帳人口 vs 選挙人名簿登録者数）
4.  区割り改定の主体とルールの明確化

「議員定数削減」そのもの（例：総定数の削減、小選挙区の議席数維持の是非）についての具体的な議論や、それに関連する論点は、この資料からは抽出できませんでした。唯一、小選挙区の議席数維持に関する言及がありますが、これは較差是正の前提条件としての言及に留まっています。

したがって、抽出されるトピックは、**「議員定数削減」**というフィルタに直接引っかかるものはなく、**「議員定数削減」の前提となる「定数配分」**に関する論点に限定されます。

```yaml
topics:
  - id: "topic_001"
    title: "小選挙区の議席数（295議席）維持の是非"
    category: "主要論点"
    summary: "一票の較差是正を行うにあたり、現在の小選挙区295議席を維持する前提で議論を進めるかどうかが論点として挙げられている。"
    spectrum:
      axis: "295議席維持 ←→ 議席数変更の可能性"
      positions:
        - label: "維持を前提とする立場"
          description: "現在の小選挙区295議席を維持する前提で較差是正を行うべきという立場。"
        - label: "議席数変更の可能性を排除しない立場"
          description: "較差是正の議論の中で、議席数の変更も視野に入れるべきという立場。"
      consensus_status: "継続検討"
      consensus_detail: "事務局の説明として論点提示されたが、この議事概要内では結論が出ていない。"
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_03.gijigaiyo.pdf"
        source_filename: "senkyoseido_03.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_03.gijigaiyo.pdf/$File/senkyoseido_03.gijigaiyo.pdf"
        source_date: "2014-10-20"
        verbatim_quote: |
           その他
          議員定数の地域への配分方式について、ヘア式最大剰余法、ラウン
          ズ方式、ドント方式、サンラグ方式、ヒル方式、ディーン方式及びア
          ダムズ方式のそれぞれの概要と特性の説明があった。
          次に、日本、アメリカ、イギリス、フランス、ドイツ及びカナダの
          各国の下院の定数配分や区割りの方法、１選挙区当たりの平均人口、
          最大選挙区と最小選挙区間の較差、有権者数などについて説明があっ
          た。
          最後に、国勢調査人口、住民基本台帳人口及び選挙人名簿登録者数
          に係る統計の概要と各統計における各都道府県の全国に対する構成比
          を用いたこれらの統計間の比較について説明があった。
      - id: "chunk_002"
        source_doc_id: "senkyoseido_03.gijigaiyo.pdf"
        source_filename: "senkyoseido_03.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_03.gijigaiyo.pdf/$File/senkyoseido_03.gijigaiyo.pdf"
        source_date: "2014-10-20"
        verbatim_quote: |
           次に、日本、アメリカ、イギリス、フランス、ドイツ及びカナダの
          各国の下院の定数配分や区割りの方法、１選挙区当たりの平均人口、
          最大選挙区と最小選挙区間の較差、有権者数などについて説明があっ
          た。
          最後に、国勢調査人口、住民基本台帳人口及び選挙人名簿登録者数
          に係る統計の概要と各統計における各都道府県の全国に対する構成比
          を用いたこれらの統計間の比較について説明があった。
          
          （２）各委員からの主な発言 
           緊急是正 （０増５減） には１人別枠方式を残しているのではないかとの批
          判があり、 較差が２倍以内におさまっているという理屈では乗り越えられ
          ないのではないか。 
           最大較差を最小化するという目標と議席を比例配分するという目標は、 同
          時に達成することが必ずしも可能ではない別の目標であるので、 ある程度
          まで両者を尊重した上で、 どこで妥協するのか、 そのためにはどのような
          配分方法があるのかということを示し、 生産的に議論ができるようにした
          い。 
           緊急是正によって削除された区画審設置法第３条第２項にかわる明確で
          簡潔な都道府県への定数配分規定を設け、 区画審が同法第３条の規定に基
          づいて区割り改定作業が行えるようにすべきである。 
           最高裁は２倍を超えると憲法上許されない一票の較差が生じたという考
          えを前提に判断を行っていると思われるが、 憲法判断の問題と立法政策と
          してどのような選挙制度がふさわしいかという問題は別の問題であり、 当
          調査会ではあるべき選挙制度を議論して提言すべきである。 
           中立的な機関が、 国民が合理性や納得性を感じられるルールに基づいて定
          期的に定数配分や区割り改定を行い、 その勧告に議会が従うことが重要で
          ある。 
           定数配分方式の検討に当たっては、 デンマーク方式、 修正サンラグ方式も
          対象に加えてほしい。 
          
           一票の較差を選挙人の投票の有する影響力と考えると、 定数配分は有権者
          数に基づいて行うべきではないのか。 その場合、 長期的にある程度の安定
          性を担保するため、 住民基本台帳ではなく国勢調査における有権者数を用
          いてはどうか。 
           国勢調査における有権者数とすると、選挙権年齢18歳引き下げが現在も
          議論されているように今後どのような変更がなされるかという懸念があ
          る。 最高裁判決においても有権者数イコールほぼ人口と示しているのであ
          るから、 国勢調査人口を基準とする方が一定タームで確定的な数字を把握
          できるので実務的には望ましいのではないか。 
           最高裁の判例を前提とする限り、 人口及び有権者数のどちらに基づいても
          合理性はあると思われるが、 立法作業を考慮すると正確な人口を基に考え
          た方が実務的にもよいのではないか。 
          
           各都道府県への定数配分方式の検討は、 将来推計人口も加味して行うべき
          である。また、従来は都道府県単位に定数を配分していたが、ブロック単
          位で配分することも検討すべきではないか。 
           定数配分をブロック単位で行っても、 ブロックの中で小選挙区の区割りを
          するに当たっては各都道府県にまた配分することになると考えられ、 ２度
          作業を行うことになってしまうのではないか。 
           都道府県への定数配分段階よりも各小選挙区の区割り段階の方が不均衡
          の度合いが大きいとなると、 不均衡は都道府県内の区割りによって発生し
          ている可能性があるということについて検討してみる必要があるかもし
          れない。 
           緊急是正で０増５減の対象となった選挙区への定数配分は平成22年国勢
          調査人口に基づいて一票の較差の是正が行われ、最大と最小については考
          えられているが、その中間部分については平成12年国勢調査によるもの
          である。 都道府県への新しい配分ルールを決めれば、区画審がこの中間部
          分を考慮して判断することになるであろう。 
           １人別枠方式について、 立法過程において地方に厚くすることがいいこと
          であるということがポジティブに説明された経緯はあるのか。 
          
           わが国では一票の較差に係る訴訟の被告は選挙管理委員会であるが、 諸外
          国においては選挙区間較差等が問題となった場合に誰が被告となってい
          るのか。 
          
          （３）次回以降の日程等の協議が行われた。 
            ① 次回のテーマ 
          「衆議院小選挙区の一票の較差」 
            ② 次回以降の日程 
              平成26年11月20日（木） 14時 
              平成26年12月11日（木） 16時 
```

---

## File: senkyoseido_04.gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "定数削減、較差縮小、比例性の確保の三者のトレードオフ"
    category: "主要論点"
    summary: "議員定数の削減、一票の較差の縮小、および比例性の確保という三つの目標は同時に達成することが困難であり、何が最も重要な基準であるかについて合意形成が必要である。"
    spectrum:
      axis: "定数削減優先 ←→ 較差縮小・比例性優先"
      positions:
        - label: "較差縮小・比例性優先派"
          description: "定数削減よりも、較差の縮小や比例性の確保を優先すべきという立場。"
        - label: "定数削減も考慮すべき派"
          description: "三つ全てを成り立たせるのは無理であるため、何が重要か合意の上で配分方式を選択すべきという立場。"
      consensus_status: "継続検討"
      consensus_detail: "何が最重要基準であるかについて合意が得られていない。"
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_04.gijigaiyo.pdf"
        source_filename: "senkyoseido_04.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_04.gijigaiyo.pdf/$File/senkyoseido_04.gijigaiyo.pdf"
        source_date: "2014-11-20"
        verbatim_quote: |
           定数を削減し、比例的にし、較差を縮小する、これらを全部成り立たせることは無理であるので、何が重要な基準であるのかという合意を得た上で、配分方式の選択の議論を進めるべきである。
        position: "較差縮小・比例性優先派"
        speaker: "各委員"
        context: "都道府県への定数配分方式選択の視点"
      - id: "chunk_002"
        source_doc_id: "senkyoseido_04.gijigaiyo.pdf"
        source_filename: "senkyoseido_04.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_04.gijigaiyo.pdf/$File/senkyoseido_04.gijigaiyo.pdf"
        source_date: "2014-11-20"
        verbatim_quote: |
           比例性を保ち、較差を縮小し、定数を削減するという３つを全て実現することは不可能であることを国民にしっかり説明すべきである。
        position: "較差縮小・比例性優先派"
        speaker: "各委員"
        context: "アダムズ方式に関する議論"

  - id: "topic_002"
    title: "定数1の都道府県の回避と補欠選挙の期間"
    category: "課題・懸念"
    summary: "定数1の都道府県では、補欠選挙が年2回（春と秋）に統一されているため、欠員発生から次の補欠まで長期間（半年程度）議員が不在となる懸念があり、少なくとも定数2を確保すべきとの意見が出ている。"
    spectrum:
      axis: "定数1容認（較差優先） ←→ 少なくとも定数2確保（安定性優先）"
      positions:
        - label: "定数2確保派"
          description: "補欠選挙の期間を考慮し、定数1は避け、最低でも2を確保すべきという立場。"
        - label: "定数1容認派"
          description: "定数2を確保することで較差が拡大する場合、1人となることを割り切る必要も生じるという立場。"
      consensus_status: "継続検討"
      consensus_detail: "定数2確保の望ましさと、それが較差拡大を招く可能性との間で判断が分かれている。"
    evidence_chunks:
      - id: "chunk_003"
        source_doc_id: "senkyoseido_04.gijigaiyo.pdf"
        source_filename: "senkyoseido_04.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_04.gijigaiyo.pdf/$File/senkyoseido_04.gijigaiyo.pdf"
        source_date: "2014-11-20"
        verbatim_quote: |
           国会議員に欠員が生じた場合の補欠選挙は年２回（春と秋）に統一して行われるので、定数１の団体において欠員が出た場合、長い場合は半年ほど議員がいない状態が生じるおそれもあり、少なくとも定数２は必要である。
        position: "定数2確保派"
        speaker: "各委員"
        context: "都道府県への定数配分方式選択の視点"
      - id: "chunk_004"
        source_doc_id: "senkyoseido_04.gijigaiyo.pdf"
        source_filename: "senkyoseido_04.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_04.gijigaiyo.pdf/$File/senkyoseido_04.gijigaiyo.pdf"
        source_date: "2014-11-20"
        verbatim_quote: |
           各県の定数を２人以上とすることは望ましいが、それによって較差が拡大するのであれば、結果として１人となることについて割り切る必要も出てくるのではないか。
        position: "定数1容認派"
        speaker: "各委員"
        context: "都道府県への定数配分方式選択の視点"

  - id: "topic_003"
    title: "都道府県間の定数配分方式の選択基準（アダムズ方式、ドント方式、サンラグ方式の比較）"
    category: "主要論点"
    summary: "都道府県への定数配分方式として、アダムズ方式（切り上げ）、ドント方式（切り捨て）、サンラグ方式（四捨五入）などが議論されており、それぞれの方式が大小の団体に与える影響（有利不利）を考慮して選択する必要がある。"
    spectrum:
      axis: "小団体有利（アダムズ） ←→ 大団体有利（ドント）"
      positions:
        - label: "小団体有利（アダムズ）支持"
          description: "アダムズ方式（切り上げ）は小さい団体に効果的であり、較差が小さくなる面もあるため良いのではないかという立場。"
        - label: "大団体有利（ドント）支持"
          description: "ドント方式（切り捨て）は大きな団体に有利であるという認識。"
        - label: "中立的（サンラグ）支持"
          description: "サンラグ方式（四捨五入）が中間的な位置にあるという認識。"
      consensus_status: "継続検討"
      consensus_detail: "小団体有利、大団体有利、中立のいずれを選ぶかが判断基準となる。"
    evidence_chunks:
      - id: "chunk_005"
        source_doc_id: "senkyoseido_04.gijigaiyo.pdf"
        source_filename: "senkyoseido_04.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_04.gijigaiyo.pdf/$File/senkyoseido_04.gijigaiyo.pdf"
        source_date: "2014-11-20"
        verbatim_quote: |
           例えばアダムズ方式（切り上げ）は小さい団体に効果的であり、ドント方式（切り捨て）は大きな団体に有利であり、 サンラグ方式 （四捨五入） がその中間に位置するのであろうが、そういう性質を持つ各方式の中から、小さな県により有利に配分される方法を選ぶのか、大きな県により有利に配分される傾向のある方法を選ぶのか、中立的なものを選ぶのか、ということが判断の基準となるのではないか。
        position: "小団体有利（アダムズ）支持"
        speaker: "各委員"
        context: "都道府県への定数配分方式選択の視点"
      - id: "chunk_006"
        source_doc_id: "senkyoseido_04.gijigaiyo.pdf"
        source_filename: "senkyoseido_04.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_04.gijigaiyo.pdf/$File/senkyoseido_04.gijigaiyo.pdf"
        source_date: "2014-11-20"
        verbatim_quote: |
           比例代表選挙における政党への議席配分については、阻止条項を入れるかどうかという問題があるので、ドント方式という大きい政党に有利な方法をあえてとった。しかし、小選挙区定数の都道府県配分のように、次のステップを考えて、都道府県間較差を小さくするとか、地域性を考慮するという意味であれば、アダムズ方式のような切り上げ方式が選挙区間の較差が小さくなる面もあり、よいのではないか。
        position: "小団体有利（アダムズ）支持"
        speaker: "各委員"
        context: "都道府県への定数配分の具体的方式"

  - id: "topic_004"
    title: "安定性の確保と選挙区の変更頻度"
    category: "主要論点"
    summary: "国民は制度の安定性を求めているため、人口が増加している団体以外は、できるだけ長い期間、同じ選挙区とすることが望ましい。配分方法の選択にあたっては、都道府県間の較差が小さく、かつ都道府県内で区割りを変更する選挙区の数が少なくなる方法が望ましい。"
    spectrum:
      axis: "安定性（変更頻度抑制）優先 ←→ 人口変動への即時対応"
      positions:
        - label: "安定性重視"
          description: "国民の安定性への要求に応えるため、区割りの変更を最小限に抑えるべきという立場。"
        - label: "人口変動対応重視"
          description: "人口が増えている団体については定数を維持できないという立場。"
      consensus_status: "両論併記"
      consensus_detail: "人口増減への対応と安定性の確保のバランスが課題。"
    evidence_chunks:
      - id: "chunk_007"
        source_doc_id: "senkyoseido_04.gijigaiyo.pdf"
        source_filename: "senkyoseido_04.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_04.gijigaiyo.pdf/$File/senkyoseido_04.gijigaiyo.pdf"
        source_date: "2014-11-20"
        verbatim_quote: |
           国民は制度の安定性も求めている。人口が増えている団体の定数がいつまでも同じでよいというわけにはいかないが、それ以外のところはなるべく長い間同じ選挙区とすることが可能かどうかも考慮すべきである。すなわち、 （配分方法については）都道府県間の較差が小さく、かつ都道府県内において区割りを変更する選挙区の数も少なくするものがよい。
        position: "安定性重視"
        speaker: "各委員"
        context: "都道府県への定数配分方式選択の視点"
```

---

## File: senkyoseido_05.gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "定数削減に伴う定数1の県発生の許容性"
    category: "主要論点"
    summary: "衆議院議員定数削減を進める過程で、人口最小県に定数1の県が生じることをどこまで許容するか、また、定数1の県を避けるために最低2議席を確保すべきかについて議論がある。"
    spectrum:
      axis: "定数1の県を許容する ←→ 定数1の県を極力避ける（最低2議席確保）"
      positions:
        - label: "定数1許容派"
          description: "定数削減を進める上では、定数1の県が生じることは避けられないと覚悟すべきであり、1人別枠と同じ問題が生じることを懸念しすぎない。"
        - label: "定数1回避派"
          description: "定数1の県をなるべく作らない、あるいは人口最小県の定数を最低2議席とすべきであり、これは上院議員数とのバランスや、選挙区割り段階での較差を小さく保つための現実的な選択である。"
      consensus_status: "継続検討"
      consensus_detail: "定数1の県を許容するか否か、またその理由付け（バランスか、較差是正か）について意見が分かれており、全体の定数次第で議論が変わる可能性も指摘されている。"
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           「定数１人の県をなるべくつくらない。 」として人口が大幅に減った場
          合にも最低２議席を確保することとすると、１人別枠と同じ問題が起こ
          る。また、定数削減の議論を進めていく中では、１議席の県が生じても
          仕方がないことをある程度覚悟すべきである。
        position: "定数1許容派"
        speaker: "委員"
        context: "定数削減と定数1県に関する議論"
      - id: "chunk_002"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           二院制議会において、 下院 （衆議院） が 「責任政府」 の関係にある中で、
          一定地域から選出する議員数について、下院議員の数が上院（参議院）
          議員よりも少なくなることは、バランス上いかがか。定数１人の県をつ
          くらないということではなく、人口最小県の下院議員定数が少なくとも
          上院議員と同数、すなわち２人とすべきである。
        position: "定数1回避派"
        speaker: "委員"
        context: "定数削減と定数1県に関する議論（バランスの観点）"
      - id: "chunk_003"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           「定数１人の県をなるべくつくらない。 」という結論だけでは誤解を招
          く。「現状の定数を前提とした場合に、都道府県ごとに定数を割り振った
          後に最終的に選挙区割りをしたときの較差をなるべく小さくするため
          には、定数１人の県はなるべく避けることが現実的な選択であるという
          実質的な理由も書くべきではないか。
        position: "定数1回避派"
        speaker: "委員"
        context: "定数削減と定数1県に関する議論（較差是正の観点）"
      - id: "chunk_004"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           憲法上「定数０（の団体）を設けない」ことは当たり前であり、そのよ
          うな制度は設けるわけにはいかないので、問題は「定数１」を許容する
          かどうかということだ。ラウンズ方式やアダムズ方式採用の議論は、定
          数１の団体をつくらないというだけでなく、なるべく少数県に有利な傾
          向を持つ方式を採用しようというものだ。 「少数県になるべく有利に」
          とはいえないので、 「定数１人の県をなるべくつくらない」となるので
          はないか。 「なるべくつくらない」であるから「絶対に２人にしなけれ
          ばならない」というわけでもない。
        position: "継続検討"
        speaker: "委員"
        context: "定数1の許容範囲に関する議論"
      - id: "chunk_005"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           （人口少数県の定数が）１人なのか２人かという議論は、全体の定数が
          どうなるのかによって議論が変わる可能性があるのではないか。
        position: "継続検討"
        speaker: "委員"
        context: "定数削減の規模と定数1県の問題の関連性"
      - id: "chunk_006"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           定数削減あるいは人口変動という要素が加わることによって全ての
          選挙区が変わる可能性があることを政治家の方々にも覚悟していただ
          く必要があるのではないか。
        position: "定数1許容派"
        speaker: "委員"
        context: "定数削減と選挙区全体の見直し"

  - id: "topic_002"
    title: "定数削減を見越した将来の人口変動への対応"
    category: "主要論点"
    summary: "定数削減を進めるにあたり、将来の人口変動（特に減少）に対応できる制度設計が必要である。現在の推計人口だけでなく、将来の推計人口まで含めて議論し、国民に説明できる合理的な選択をすることが求められている。"
    spectrum:
      axis: "現行人口ベースの是正 ←→ 将来人口変動を見越した設計"
      positions:
        - label: "将来志向派"
          description: "平成42年の推計人口まで含め、将来の人口変動に対応できる制度設計をすべきであり、国民の目線から見て合理的で説明がつくものを選ぶべき。"
        - label: "現行ベース派"
          description: "（言及なし、対立軸として設定）"
      consensus_status: "継続検討"
      consensus_detail: "将来の人口変動を考慮に入れるべきという認識は共有されているが、具体的にどの時点の人口を基準とするか、またそれが制度設計にどう反映されるべきかについて、総合的な判断が必要とされている。"
    evidence_chunks:
      - id: "chunk_007"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           将来の人口変動（減少）にも、ある程度対応できるものとする
          こととし、以上の観点からラウンズ方式、アダムズ方式を中心にさら
          に検討を進めること、について説明があった。
        position: "将来志向派"
        speaker: "事務局"
        context: "配分方式検討の条件"
      - id: "chunk_008"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           較差是正の方途を考えるときに、人口減少、都市化の話は避けられな
          い。平成42年の推計人口まで含めて議論をしているが、国民の目線か
          ら見たときに、課題とされていることにどれだけ対応できるかという
          ことが非常に重要である。それらをクリアし得る可能性が最も高いも
          のを選ぶのが国民の目線から見て合理的で説明がつくものである。
        position: "将来志向派"
        speaker: "委員"
        context: "将来人口変動への対応の重要性"
      - id: "chunk_009"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           現時点でどの方式が一番較差が少ないのか、議席の数を減らしたとき
          にどうか、そして、人口変動を考慮するとどうか、などを総合的に判
          断すべきであり、議席数と将来の人口変動までを見越して制度を設計
          したという説明をすることが国民にとって意味があると思われる。
        position: "将来志向派"
        speaker: "委員"
        context: "総合的な判断の必要性"

  - id: "topic_003"
    title: "定数削減に伴う選挙区区割りの見直し範囲"
    category: "課題・懸念"
    summary: "定数削減や人口変動を理由に区割りを改定する場合、緊急是正（平成25年改定）のように限定的な見直しに留めるべきか、あるいは全選挙区を対象として新たな視点で議論すべきかという点について、政治家の覚悟が問われている。"
    spectrum:
      axis: "限定的な見直し ←→ 全選挙区の抜本的見直し"
      positions:
        - label: "限定的見直し派"
          description: "平成25年改定のように、緊急是正として必要最小限の改定に留めるべき。"
        - label: "全選挙区見直し派"
          description: "定数削減や人口変動により全ての選挙区が変わる可能性があることを覚悟し、全選挙区を対象として議論することが基本になるべき。"
      consensus_status: "継続検討"
      consensus_detail: "定数配分の見直しが行われ人口がフラットになった場合、区割り審議会はより人口に配慮した新しい区割りができるという期待がある一方で、政治家側には区割り変更の覚悟が必要とされている。"
    evidence_chunks:
      - id: "chunk_010"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           平成 25 年区割り改定は、緊急是正であることから必要最小限の改定
          とされたものであり、全部を見直して新たな視点で検討するものでは
          なかった。 （区割り改定に当たっては）全選挙区を対象として議論す
          ることが基本になるべきであり、その中で２倍をめどに、できるだけ
          差が少なくなるようにすべきである。
        position: "全選挙区見直し派"
        speaker: "委員"
        context: "区割り改定の基本方針"
      - id: "chunk_011"
        source_doc_id: "senkyoseido_05.gijigaiyo.pdf"
        source_filename: "senkyoseido_05.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_05.gijigaiyo.pdf/$File/senkyoseido_05.gijigaiyo.pdf"
        source_date: "2015-02-09"
        verbatim_quote: |
           定数削減あるいは人口変動という要素が加わることによって全ての
          選挙区が変わる可能性があることを政治家の方々にも覚悟していただ
          く必要があるのではないか。
        position: "全選挙区見直し派"
        speaker: "委員"
        context: "定数削減に伴う区割り変更の覚悟"
```

---

## File: senkyoseido_06.giijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "定数削減の是非と背景にある議論"
    category: "主要論点"
    summary: "定数削減の必要性について、与党側は改革の一環として推進する一方、野党の一部（共産、社民）は削減に反対し、選挙制度の抜本改革（比例代表中心への変更）を主張している。また、定数削減が「身を切る改革」の唯一の手段と見なされることへの疑問も呈されている。"
    spectrum:
      axis: "定数削減推進 ←→ 定数削減反対・制度改革優先"
      positions:
        - label: "定数削減推進派（与党・一部野党）"
          description: "定数削減（特に比例定数削減や小選挙区定数削減）を、現行制度維持の前提として進めるべき改革と位置づけている。"
        - label: "定数削減反対派（共産・社民）"
          description: "定数削減には反対し、比例代表中心の制度への抜本改革を主張している。"
      consensus_status: "両論併記"
      consensus_detail: "与党案（比例定数30削減）と野党案（小選挙区定数削減を含む案、共産・社民案は削減反対）が対立している。"
    evidence_chunks:
      - id: "chunk_001_1"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          第47回総選挙における公約等では、与党である自民、 公明は、過去の与党案への言及を行いつつも本調査会の答申を 尊重するとしたこと、野党については、民主は、身を切る改革、一票の 較差是正、定数削減の実現を、維新は、議員歳費の３割カットと併せ、 議員定数の３割削減を、次世代は、定数削減を、共産、社民は、定数削
          減に反対しつつ、比例代表選挙中心の制度への変更を、それぞれ掲げて
          いること、
        position: "定数削減推進派（与党・一部野党）"
        speaker: "事務局"
        context: "各党の選挙公約の紹介"
      - id: "chunk_001_2"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          与党案は、小選挙区比例代表並立制の枠組を基本的に維持した上で、比例定数を30削減し、その際に、①現行11ブロックの８ブロックへの再編、②比例定数の第１配分枠90、第２配分枠60への分 割、③第１配分枠の従来通りの全政党へのドント方式による配分、④第２配分枠の比例１位の政党を除外した比例２位以下の政党へのドント 方式による配分、とするものであること、
        position: "定数削減推進派（与党・一部野党）"
        speaker: "事務局"
        context: "与党案の概要（比例定数30削減）"
      - id: "chunk_001_3"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          共産党案、 社民党案は、いずれも定数削減に反対であり、共産は、全国11ブロックによる比例 代表制への変更をすること、 社民は、比例代表中心の選挙制度への抜本 改革をすること、を内容としていること、
        position: "定数削減反対派（共産・社民）"
        speaker: "事務局"
        context: "共産党案・社民党案の概要（定数削減反対と比例代表中心への変更）"
      - id: "chunk_001_4"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          「身を切る改革」や「政治への信頼の回復」の手段は定数削減だけな
          のか。
        position: "その他"
        speaker: "委員"
        context: "定数削減を唯一の改革手段とすることへの疑問"
      - id: "chunk_001_5"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          定数削減は選挙制度の設計や議会運営にも大きな影響を及ぼすと思
          われるにもかかわらず、身を切る改革の手段として定数削減だけがい
          われるのはなぜか。
        position: "その他"
        speaker: "委員"
        context: "定数削減が議会運営に与える影響を考慮すべきとの指摘"
      - id: "chunk_001_6"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          議席は有権者にとっては選ぶ権利であるという観点からすれば、議席 を簡単に減らすことが許されるかという観点も重要である。
        position: "その他"
        speaker: "委員"
        context: "定数削減が有権者の選ぶ権利に与える影響についての懸念"
      - id: "chunk_001_7"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          衆議院議員の定数改定の経緯について、
        position: null
        speaker: "事務局"
        context: "定数削減の背景となる経緯の説明"
      - id: "chunk_001_8"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          委員会数や委員会の定数を維持しながら定数を減らした場合には、この率が高まること、等についての説明があっ た。
        position: "その他"
        speaker: "事務局"
        context: "定数削減が委員会兼務率に与える影響"

  - id: "topic_002"
    title: "定数削減方法に関する具体的な提案の比較"
    category: "主要論点"
    summary: "定数削減の具体的な方法について、与党案は比例定数のみの削減（30削減）を提案し、野党案（民主・維新・みんな・結い・生活）は小選挙区定数削減を主軸とする案（A案：25削減、B案：15削減）を提示しており、削減対象と削減幅に大きな隔たりがある。"
    spectrum:
      axis: "比例定数削減（与党案） ←→ 小選挙区定数削減（野党案）"
      positions:
        - label: "与党案（比例定数削減）"
          description: "小選挙区比例代表並立制の枠組みを維持し、比例定数を30削減する案。"
        - label: "野党案（小選挙区定数削減）"
          description: "小選挙区の定数削減を主軸とし、総定数削減幅が15～25となる案。"
      consensus_status: "継続検討"
      consensus_detail: "削減対象（小選挙区か比例代表か）および削減幅について、各党案が併存しており、合意に至っていない。"
    evidence_chunks:
      - id: "chunk_002_1"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          与党案は、小選挙区比例代表並立制の枠組を基本的に維持した上で、比例定数を30削減し、その際に、①現行11ブロックの８ブロックへの再編、②比例定数の第１配分枠90、第２配分枠60への分 割、③第１配分枠の従来通りの全政党へのドント方式による配分、④第２配分枠の比例１位の政党を除外した比例２位以下の政党へのドント 方式による配分、とするものであること、
        position: "与党案（比例定数削減）"
        speaker: "事務局"
        context: "与党案の概要（比例定数30削減）"
      - id: "chunk_002_2"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          野党５党案（民主、維新、みん な、結い、生活）は２案併記であり、いずれも小選挙区の定数削減を 行うものであるが、Ａ案は、定数を25削減した上で各都道府県への配分は最大剰余法によって行い、 結果として５増30減、 最大較差は1.877 倍となるものであり、Ｂ案は、各都道府県に人口50万人当たり定数１ を配分し、50万人以下は定数１とし、結果として３増18減で総定数15 減、 最大較差は1.692倍となるものであること、
        position: "野党案（小選挙区定数削減）"
        speaker: "事務局"
        context: "野党5党案の概要（小選挙区定数削減を主軸とする案）"
      - id: "chunk_002_3"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          平成26年の解散・総選挙後、 同年12月に提出された維新の法案は、総定数を475から336に約３割 削減するものであり、 この削減の内訳は小選挙区が55、 比例代表が84、 となっていること、
        position: "野党案（小選挙区定数削減）"
        speaker: "事務局"
        context: "維新の党の法案概要（大幅な総定数削減）"

  - id: "topic_003"
    title: "定数削減と一票の格差是正・民意集約機能のバランス"
    category: "課題・懸念"
    summary: "定数削減は一票の格差是正や民意集約機能の緩和といった選挙制度設計上の他の論点と密接に関連しており、定数削減のみを先行させることへの懸念や、削減後の制度設計への配慮が求められている。"
    spectrum:
      axis: "格差是正優先 ←→ 民意集約機能維持優先"
      positions:
        - label: "格差是正・制度改革優先"
          description: "定数削減と一票の格差是正をセットで進めるべきという立場。"
        - label: "民意集約機能維持優先"
          description: "定数削減により民意集約機能が行き過ぎたものにならないよう配慮すべきという立場。"
      consensus_status: "継続検討"
      consensus_detail: "定数削減の議論が、一票の価値や民意集約機能の緩和の問題と切り離せない状況にある。"
    evidence_chunks:
      - id: "chunk_003_1"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          同年 11 月、自民、公明、民主の３党間で定数削減を含め、さらなる改革が必要
          であり、 中長期的な課題である選挙制度のあるべき姿の検討とは切り離
          して、小選挙区比例代表並立制の当面の維持、定数削減と小選挙区の民
          意集約機能が行き過ぎたものにならないよう配慮することが確認され
          た。
        position: "民意集約機能維持優先"
        speaker: "事務局"
        context: "定数削減と小選挙区の民意集約機能への配慮の確認"
      - id: "chunk_003_2"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          平成25年6月25日、 「選挙制度に関する与野党実務 者協議」 に出席する全ての党で、 現行並立制の功罪を広く評価 ・ 検証し、 定数削減、一票の価値、民意集約機能の緩和の問題を含め、抜本的な見直しは参議院選挙後に協議するとの確認事項が文書化された。
        position: "格差是正・制度改革優先"
        speaker: "事務局"
        context: "定数削減、一票の価値、民意集約機能の緩和が一体の課題として認識されていたこと"
      - id: "chunk_003_3"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          現行制度は民意の集約としての小選挙区制と民意の反映としての比 例代表制を組み合わせたものであり、６対４で民意の集約機能が大き いが、そこをどのように調整していくかという観点で比例代表部分を 検討するのがソフトランディングの方法としてあり得る。
        position: "民意集約機能維持優先"
        speaker: "委員"
        context: "現行制度のバランス（集約機能6割、反映機能4割）を念頭に置いた調整の必要性"
      - id: "chunk_003_4"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          また、民意の集約が過度に進むことを懸念しながら比例定数を削減しようという理由が理解できない。
        position: "格差是正・制度改革優先"
        speaker: "委員"
        context: "民意集約が進みすぎることへの懸念があるにもかかわらず比例定数を削減する論理への疑問"

  - id: "topic_004"
    title: "定数削減と議会運営への影響（委員会兼務率の上昇）"
    category: "課題・懸念"
    summary: "定数削減が実施された場合、議員一人当たりの委員会兼務率が上昇し、議会運営に影響を及ぼす懸念がある。特に、委員会数や定数を維持したまま定数を減らすと、この傾向が顕著になる。"
    spectrum:
      axis: "定数削減による影響（懸念） ←→ 影響を許容する"
      positions:
        - label: "懸念あり"
          description: "定数削減が委員会兼務率の上昇を通じて議会運営に悪影響を及ぼすことを懸念する立場。"
        - label: "影響を許容"
          description: "定数削減の必要性を優先し、発生しうる運営上の影響は許容すべきとする立場（文書内では明確な反対意見は見られないが、事実として指摘されている）。"
      consensus_status: "継続検討"
      consensus_detail: "定数削減が委員会兼務率に与える影響は事実として指摘されており、今後の設計で考慮すべき点である。"
    evidence_chunks:
      - id: "chunk_004_1"
        source_doc_id: "senkyoseido_06.giijigaiyo.pdf"
        source_filename: "senkyoseido_06.giijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_06.giijigaiyo.pdf/$File/senkyoseido_06.giijigaiyo.pdf"
        source_date: "2015-03-03"
        verbatim_quote: |
          衆議院議員は、平均で2.33の委員会を兼務しており、与党は行政府の職 に就いている議員の代わりに兼務が必要となる場合があることにより、 兼務の率はこれを上回ること、 委員会数や委員会の定数を維持しながら 定数を減らした場合には、この率が高まること、等についての説明があっ た。
        position: "懸念あり"
        speaker: "事務局"
        context: "定数削減が委員会兼務率を上昇させるメカニズムの説明"
```

---

## File: senkyoseido_07.gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "比例代表定数の削減案と枠組みの設計"
    category: "主要論点"
    summary: "比例代表定数を30議席削減し、150議席とする案（自民党案）について、その内訳（第1比例枠90議席、第2比例枠60議席）の根拠と、少数政党への配慮の仕方が論点となっている。"
    spectrum:
      axis: "第1枠中心（自民党案） ←→ 比例定数削減のあり方（公明党の連用制志向）"
      positions:
        - label: "自民党案（第1・第2枠分割）"
          description: "比例定数を30減らし150議席とし、90議席（第1枠）を全政党に得票数割で、60議席（第2枠）を比例2位以下に得票数割で配分する案。少数政党への影響を抑えるため。"
        - label: "比例定数削減への慎重論"
          description: "単純な比例定数削減は民意の反映機能の低下を招くため、小選挙区削減を優先すべき、あるいは連用制など制度変更を伴うべきとの意見。"
      consensus_status: "継続検討"
      consensus_detail: "自民党案の第2枠の具体的な効果や、公明党が主張する連用制への移行の是非が未解決。"

    evidence_chunks:
      - id: "chunk_001_1"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           小選挙区比例代表並立制を維持した上で、比例代表の議席数を
          30議席減少させ150議席とし、その場合に、比例ブロックを現
          在の11ブロックから８ブロックに再編するとともに、150議席
          を90議席と60議席に分割し、90議席（第１比例枠）を全政党
          を対象に比例代表の得票数割で、60議席（第２比例枠）を比例
          ２位以下の政党にそれらに係る比例代表の得票数割で、それぞ
          れ配分する案を策定し、2013年（平成25年）3月28日、自民・
          公明両党で合意している。
        position: "自民党案（第1・第2枠分割）"
        speaker: "細田博之 議員"
        context: "自民党の意見陳述（比例定数削減案）"
      - id: "chunk_001_2"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           比例代表の議席を第１枠（90 議席）と第２枠（60 議席）に分
          ける根拠は何かとの問いに対し、比例定数を30 減らしても、
          全体として少数政党に影響が出ないようにしたものである旨
          の回答があった。
        position: "自民党案（第1・第2枠分割）"
        speaker: "細田博之 議員"
        context: "調査会委員からの質問への回答"
      - id: "chunk_001_3"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           現行制度では得票率と獲得議席数とが大きく乖離しており、
          小選挙区の行き過ぎた民意の集約機能を是正し、より民意の反
          映を重視した制度に見直さなければならないという観点から、
          単純に比例定数の削減を行おうとすることは到底認められな
          い。
        position: "比例定数削減への慎重論"
        speaker: "北側一雄 議員"
        context: "公明党の意見陳述（比例定数削減への懸念）"

  - id: "topic_002"
    title: "議員定数削減の規模と優先順位"
    category: "主要論点"
    summary: "議員定数削減の規模について、維新の党は3割削減（480→336）を主張する一方、民主党は小選挙区15減（295→280）を提案し、自民党案は比例30減に留まるなど、削減幅に大きな隔たりがある。また、定数削減を最優先課題とするかについても意見が分かれている。"
    spectrum:
      axis: "大幅削減（維新案3割減） ←→ 較差是正を優先した小幅削減（民主党案15減）"
      positions:
        - label: "大幅削減推進派（維新）"
          description: "財政状況を鑑み、国会自らが身を切る改革の第一歩として3割削減（小選挙区240、比例96）を主張。"
        - label: "較差是正優先派（民主）"
          description: "定数削減は較差是正とセットで、将来の人口減を見据え小選挙区を15削減（280）し、比例も3対2の比率で削減すべき。削減は国民との約束として優先。"
        - label: "制度改革の中での削減派（公明）"
          description: "定数削減は抜本改革の中で行うべきだが、当面は自公案（比例30減）もやむなしとするが、単純な比例定数削減は民意の反映を損なうため反対。"
      consensus_status: "継続検討"
      consensus_detail: "削減の規模（3割減か、15減か）と、削減の根拠（身を切る改革の第一歩か、較差是正の手段か）について合意に至っていない。"

    evidence_chunks:
      - id: "chunk_002_1"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           衆議院議員の定数を480（平成24年における定数） から３割削
          減して336人とし、小選挙区を240人（55人削減） 、比例代表
          を96人（84人削減）する改正案を国会（衆議院）に提出して
          いる。
        position: "大幅削減推進派（維新）"
        speaker: "松野頼久 議員"
        context: "維新の党の意見陳述（定数3割削減案）"
      - id: "chunk_002_2"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           小選挙区は、 各都道府県について人口50万人当たり定数１を人
          口比例で配分し（３増18減） 、結果的に定数を15削減する（小
          選挙区定数280）。
        position: "較差是正優先派（民主）"
        speaker: "枝野幸男 議員"
        context: "民主党の意見陳述（小選挙区定数削減案）"
      - id: "chunk_002_3"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           定数削減は、 （平
          成 24 年の）党首討論において、 第１党と第２党の党首が国民
          の前で約束したことであり、これが実現されなければ政治不信
          はますます拡大するので、まずはこれを実現しなければならな
          いと考えている旨の回答があった。
        position: "較差是正優先派（民主）"
        speaker: "枝野幸男 議員"
        context: "定数削減の優先度に関する質問への回答"

  - id: "topic_003"
    title: "一票の較差測定基準と選挙区割りへの影響"
    category: "主要論点"
    summary: "一票の較差を測る基準について、流動的な有権者数ではなく、国勢調査人口（ただし外国籍人口を除く）を用いるべきという主張がある。また、都道府県内の選挙区割りについて、較差2倍未満の維持のためには、市区町村の分割を積極的に行うこともやむを得ないという見解が示されている。"
    spectrum:
      axis: "国勢調査人口（外国籍除く）基準 ←→ 従来の基準（住民票等）"
      positions:
        - label: "国勢調査人口（外国籍除く）基準採用派"
          description: "較差の基準は最も権威ある統計である国勢調査人口（外国籍人口を除く）によるべき。"
        - label: "選挙区割りの柔軟性容認派"
          description: "較差2倍未満を安定的に実現するため、市区町村の分割を積極的に行うこともやむを得ない。"
      consensus_status: "両論併記"
      consensus_detail: "較差の基準については国勢調査人口（外国籍除く）が提案されたが、選挙区割りの手法については安定性と較差是正のトレードオフが残る。"

    evidence_chunks:
      - id: "chunk_003_1"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           較差を測る基準については、18歳選挙権実現等によって大きく
          変動する可能性がある有権者数や、転勤や大学入学等による異
          動があり非常に流動的な住民票による数ではなく、国民の数に
          ついての最も権威のある統計である国勢調査の結果による人
          口によるべきである。ただし、国勢調査人口には（投票権を持
          ち得ない）外国籍人口が入っているが、較差を考える上で、本
          来対象にすべきではないので、国勢調査の数からこれを除外し
          たものを用いるべきである。
        position: "国勢調査人口（外国籍除く）基準採用派"
        speaker: "細田博之 議員"
        context: "自民党の意見陳述（一票の較差の基準）"
      - id: "chunk_003_2"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           都道府県内の選挙区割りの在り方についてどう考えるかとの
          問いに対し、較差が２倍を切りさえすればよいという従来の法
          令の規定を改め、原則として1.9倍にせよというようなことを
          規定すれば、区画改定後10 年間に人口異動があっても最大較
          差が２倍を超えるおそれはなくなる、選挙区間の較差は市区
          町村の区割り（区割りに際して市区町村の分割をどのように
          行うか）により生ずるものであり、市区町村の分割をもっと
          積極的に行ってもよい、旨の回答があった。
        position: "選挙区割りの柔軟性容認派"
        speaker: "細田博之 議員"
        context: "調査会委員からの質問への回答（選挙区割り）"
      - id: "chunk_003_3"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           較差２倍未満を安定的に実現することが憲法上の最大の目的であ
          って、そのために多少区割りにお
          いて行政区の中で分かれることは我慢していただきたいと申
          し上げ了解いただいていると考えている旨の回答があった。
        position: "選挙区割りの柔軟性容認派"
        speaker: "細田博之 議員"
        context: "選挙区の安定性に関する質問への回答"

  - id: "topic_004"
    title: "小選挙区と比例代表の定数比率の考え方"
    category: "主要論点"
    summary: "現行制度創設時の小選挙区と比例代表の定数比率（3対2）を、定数削減の際の配慮基準として用いるかどうかが論点となっている。民主党はこれを基本とするが、維新の党は小選挙区中心を維持するため、比例削減をより大きくすべきと主張している。"
    spectrum:
      axis: "制度創設時の比率（3:2）維持（民主党） ←→ 小選挙区優先（維新）"
      positions:
        - label: "3:2比率維持派（民主）"
          description: "小選挙区制度の民意集約機能が行き過ぎないよう、現行制度創設時の3対2の比率に配慮して削減すべき。"
        - label: "小選挙区優先派（維新）"
          description: "政権選択の選挙であるため小選挙区の定数を多くすべきであり、比例代表の定数をより大きく削減すべき。"
      consensus_status: "両論併記"
      consensus_detail: "民主党は3:2比率を合意可能な根拠とするが、維新の党は小選挙区を優先し、比例削減をより大きくすべきと主張しており、比率の適用方法で意見が異なる。"

    evidence_chunks:
      - id: "chunk_004_1"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           小選挙区と比例の双方を削減。その際、小選挙区制度の民意集約機能が行き過ぎたものとならないよ
          う小選挙区と比例の定数の比率を配慮
        position: "3:2比率維持派（民主）"
        speaker: "枝野幸男 議員"
        context: "民主党の意見陳述（定数削減の考え方）"
      - id: "chunk_004_2"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           制度創設時の小選挙区定数と比例代表定数の比率（３対２）に
          配慮することとした根拠は何かとの問いに対し、抜本改正でな
          いので現在の制度創設時の比率に根拠を求めるのが最も合意
          が可能であるという政治的な判断である旨の回答があった。
        position: "3:2比率維持派（民主）"
        speaker: "枝野幸男 議員"
        context: "調査会委員からの質問への回答"
      - id: "chunk_004_3"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           衆議院は政権選択の選挙である以上、民意の集約を目的とした
          小選挙区の定数を多くすべきであり、国会に提出している定数
          ３割削減の改正案も小選挙区より比例代表の定数を削減する
          という考えに基づいている（注：同改正案は小選挙区比例代表並立制
          を維持）。将来の選挙制度のあり方として、小選挙区中心の制度
          を維持したい。
        position: "小選挙区優先派（維新）"
        speaker: "松野頼久 議員"
        context: "維新の党の意見陳述（選挙制度）"

  - id: "topic_005"
    title: "比例代表における惜敗率復活当選の是非"
    category: "課題・懸念"
    summary: "比例代表の議席配分において、惜敗率による復活当選の仕組みが国民に分かりにくいという指摘があり、政党が名簿順位を決める方式が比例代表制の趣旨にふさわしいのではないかという意見が出ている。"
    spectrum:
      axis: "惜敗率復活当選の容認 ←→ 名簿順位決定の徹底"
      positions:
        - label: "惜敗率復活容認派"
          description: "制度の一つの仕組として許容される範囲。"
        - label: "名簿順位決定推奨派"
          description: "惜敗率は国民から見て非常にわかりにくく、比例代表制の趣旨からは各政党が名簿順位を決める方法がふさわしい。"
      consensus_status: "継続検討"
      consensus_detail: "惜敗率復活当選の是非、および復活当選が国民に分かりにくいという懸念について、制度設計上の論点として認識されている。"

    evidence_chunks:
      - id: "chunk_005_1"
        source_doc_id: "senkyoseido_07.gijigaiyo.pdf"
        source_filename: "senkyoseido_07.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_07.gijigaiyo.pdf/$File/senkyoseido_07.gijigaiyo.pdf"
        source_date: "2015-03-25"
        verbatim_quote: |
           比例代表制は、基本的には政党が（順位づけをした）名簿をつ
          くって行う制度であるにもかかわらず、同一順位に候補者を並
          べて惜敗率で当選者を決めるという比例の使い方をしている
          政党もあることについて、また、惜敗率による復活当選につい
          て、どのように考えるか、との問いに対し、公明党は近年、重
          複立候補を行っておらず、惜敗率というのは国民から見て非常
          にわかりにくく、比例代表制の趣旨からは各政党が名簿順位を
          決める方法がふさわしいのではないかと思うが、惜敗率で当選
          順位を決める方法を否定するわけではなく、制度の一つの仕組
          として許容される範囲ではないか、復活当選は国民から見て非
          常にわかりにくく議論されてしかるべきであろう、との回答が
          あった。
        position: "名簿順位決定推奨派"
        speaker: "北側一雄 議員"
        context: "惜敗率復活当選に関する質問への回答"
```

---

## File: senkyoseido_08.gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "議員定数削減の是非と根拠"
    category: "主要論点"
    summary: "議員定数削減の必要性について、各党派で賛否が分かれており、その根拠として、国民の代表としての機能維持、政府監視機能の確保、歴史的・国際的な比較、そして消費税増税との関連付けなどが議論されている。"
    spectrum:
      axis: "定数削減賛成 ←→ 定数削減反対"
      positions:
        - label: "削減賛成派（次世代、生活）"
          description: "定数削減は可能であり、行うべきである。国会運営に支障はない、あるいは国民の要請に応える姿勢を示すべき。"
        - label: "削減反対派（共産、社民）"
          description: "定数削減は、国民の声を切り捨てることになり、国会の政府監視機能が低下するため反対。歴史的・国際的に見ても議員数は少ない。"
      consensus_status: "両論併記"
      consensus_detail: "日本共産党と社会民主党は定数削減に明確に反対しているのに対し、次世代の党と生活の党と山本太郎となかまたちは削減を主張している。新党改革は削減の必要性は認めつつも、削減しすぎると較差是正が難しくなるため削減数には言及していない。"

  - id: "topic_002"
    title: "定数削減と一票の較差是正・機能維持との関係"
    category: "課題・懸念"
    summary: "定数削減を行う場合、一票の較差是正が困難になる可能性や、国会の審議機能（委員会の質疑など）が低下する懸念が指摘されている。特に中選挙区制への移行を提案する立場からは、定数削減と較差是正を同時に行うべきとの意見がある。"
    spectrum:
      axis: "定数削減優先 ←→ 機能維持・較差是正優先"
      positions:
        - label: "定数削減と較差是正の同時検討派（新党改革）"
          description: "中選挙区制への改正の中で、一票の較差是正と定数削減をあわせて行うべき。"
        - label: "機能維持・較差是正優先派（共産、社民）"
          description: "定数削減は国会の監視機能低下や較差是正の困難化を招くため、反対。"
      consensus_status: "継続検討"
      consensus_detail: "新党改革は、中選挙区制の下で較差是正を優先しつつ定数を見るのが無難としているが、他の党派は定数削減自体に反対しているため、定数削減の是非と較差是正のバランスが論点となっている。"

  - id: "topic_003"
    title: "定数削減の具体的な基準と規模感"
    category: "主要論点"
    summary: "定数削減の議論において、具体的な削減目標や、削減の基準となる理論的根拠（例：過去の人口比率、国際比較）が提示されている。また、削減の規模についても意見が分かれている。"
    spectrum:
      axis: "大幅削減（次世代） ←→ 削減反対（共産、社民）"
      positions:
        - label: "削減容認派（次世代、生活）"
          description: "定数削減は可能であり、国会は現在ほどの定数がなくても十分に運営できる。"
        - label: "削減反対派（共産、社民）"
          description: "現行定数475は歴史的にも国際的にも少なく、削減の合理的な根拠はない。"
      consensus_status: "両論併記"
      consensus_detail: "次世代の党は定数削減に賛成し、生活の党は野党5党案に基づき削減を検討しているが、共産党と社民党は削減に強く反対している。共産党は1925年（12万人に1議席）や諸外国（10万人に1議席）との比較を根拠に現行定数475を擁護している。"

  - id: "topic_004"
    title: "定数削減が国会運営の質に与える影響"
    category: "課題・懸念"
    summary: "議員数の削減が、議員の専門性の低下や委員会での質疑の質の低下を招く可能性が懸念されている。議員が兼務する委員会の数が増え、勉強時間がなくなるという指摘がある。"
    spectrum:
      axis: "質的低下の懸念あり ←→ 質的低下の懸念なし"
      positions:
        - label: "懸念あり派（共産、次世代の指摘への回答）"
          description: "議員を減らすと、議員は常任委員会や特別委員会を兼務せざるを得なくなり、質的低下を招く。"
        - label: "懸念なし派（次世代の主張）"
          description: "議員数を減らしても国会は十分に運営できる。"
      consensus_status: "両論併記"
      consensus_detail: "共産党は、議員削減が質的低下を招くというメディアの批判的な見解を紹介しつつ、削減に反対する論拠としている。次世代の党は削減可能としているが、議員の質的低下の指摘も受けている。"

  - id: "topic_005"
    title: "定数削減と消費税増税の関連付け"
    category: "課題・懸念"
    summary: "一部の議論において、定数削減が消費税増税とセットで議論されることに対し、反対意見が表明されている。定数削減は議員自身の問題であり、国民負担増とは別問題であるという主張。"
    spectrum:
      axis: "関連付けを容認 ←→ 関連付けに反対"
      positions:
        - label: "関連付けに反対派（共産、社民）"
          description: "消費税増税の是非と定数削減は全く別の問題であり、リンクさせるのは不当であり筋違い。"
        - label: "関連付けを容認/言及なし"
          description: "定数削減を主張する側からは、この点に関する明確な反対意見は示されていない（次世代、生活、新党改革）。"
      consensus_status: "両論併記"
      consensus_detail: "共産党と社民党は、定数削減を消費税増税と結びつける動きを明確に批判している。"

  - id: "topic_006"
    title: "定数削減の議論の前提としての「政治改革」検証"
    category: "主要論点"
    summary: "定数削減の議論は、20年前に導入された「政治改革」（小選挙区比例代表並立制の導入、企業・団体献金の温存、政党助成制度の創設）の検証とセットで行うべきであるという主張がある。"
    spectrum:
      axis: "政治改革検証と同時並行 ←→ 定数削減の独立議論"
      positions:
        - label: "同時検証派（共産）"
          description: "定数の問題は、20年前の「政治改革」の時に一緒に議論された政党助成金、企業・団体献金の問題とともに検証、議論すべき。"
        - label: "独立議論派（他党派）"
          description: "定数削減や選挙制度改革を独立した論点として議論している。"
      consensus_status: "継続検討"
      consensus_detail: "共産党は、定数削減を過去の政治改革の総括の中で議論すべきとしており、議論の前提が異なっている。"

  - id: "topic_007"
    title: "定数削減の設計：比例代表定数と小選挙区定数の比率・削減方法"
    category: "主要論点"
    summary: "定数削減を行う場合、小選挙区と比例代表の定数の比率をどうするか、また、削減をどちらの区分から行うかについて具体的な提案がなされている。"
    spectrum:
      axis: "小選挙区中心削減 ←→ 比例代表削減反対"
      positions:
        - label: "小選挙区中心削減派（次世代、生活）"
          description: "小選挙区定数を削減し（次世代は15削減案を支持）、比例代表定数も削減する（生活は削減幅は調査会に委ねる）。次世代は小選挙区6：比例代表4の比率を維持すべきとしている。"
        - label: "比例代表削減反対派（社民）"
          description: "民意の的確な反映のため、比例代表定数の削減は容認できない。"
      consensus_status: "両論併記"
      consensus_detail: "次世代の党は小選挙区定数削減を前提とし、生活の党も野党5党案に基づき小選挙区定数削減を提案しているが、社民党は比例定数削減に強く反対しており、削減の対象と規模について意見が対立している。"

  - id: "topic_008"
    title: "中選挙区制導入による定数削減の可能性"
    category: "主要論点"
    summary: "新党改革は、新たな中選挙区制度（3人区を想定）への移行を提案しており、これにより30から80程度の定数削減が可能になると試算している。"
    spectrum:
      axis: "中選挙区制による削減 ←→ 現行制度維持・比例制移行"
      positions:
        - label: "中選挙区制提案派（新党改革）"
          description: "中選挙区制（3人区）を導入すれば、定数を30から80程度削減できる。"
        - label: "比例制移行派（共産）"
          description: "小選挙区制を廃止し、比例代表制へ抜本改革すべき。"
      consensus_status: "継続検討"
      consensus_detail: "新党改革は中選挙区制を定数削減の手段として提案しているが、他の主要な意見は比例代表制への移行（共産）か、現行制度の維持・微調整（次世代）である。"

evidence_chunks:
  - id: "chunk_001_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       選挙は民主主義の根幹である。国民、有権者の問題である選挙
      制度の基本原則は、国民の多様な民意をできる限り正確に反映
      することでなければならない。
       衆議院選挙制度については、現行の小選挙区比例代表並立制を
      廃止し、 民意を正確に反映する比例代表制への抜本改革を行う。
      現行の総定数を維持し、 全国11ブロックを基礎とした比例代表
      制にすることを提案している。
    position: "削減反対派（共産、社民）"
    speaker: "穀田恵二 議員（日本共産党）"
    context: "選挙制度に関する意見陳述"

  - id: "chunk_001_2"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       定数削減に反対である。
       国会議員は主権者の民意反映のためにある。「身を切る改革」
      は、その議員を削減して国民の声を切り捨てた上、消費税増税
      という負担を国民に押し付けようというものである。
    position: "削減反対派（共産、社民）"
    speaker: "穀田恵二 議員（日本共産党）"
    context: "議員定数に関する意見陳述"

  - id: "chunk_001_3"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       憲法に定められた国会の政府監視機能が定数削減により低下
      する。
       現行の衆議院議員の定数475は人口約27 万人に１議席の割合
      である。男子普通選挙権制定時は12 万人に１議席を配分して
      いた。 また、 諸外国の下院は10万人に１議席の水準であって、
      歴史的にみても国際的にみても、日本は議員が少ない国であり、
      これ以上、 「国民の代表」を削減する定数削減を行うことに合
      理的根拠は存在しない。
    position: "削減反対派（共産、社民）"
    speaker: "穀田恵二 議員（日本共産党）"
    context: "議員定数に関する意見陳述"

  - id: "chunk_002_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       定数を削減することとし、削減に当たっては、現在の比例代表
      制と小選挙区制の両方から案分して減らすこととすべきである。
       定数の削減については、当調査会の意見を尊重しなければなら
      ないと考えている。
    position: "削減容認派（次世代）"
    speaker: "園田博之 議員（次世代の党）"
    context: "議員定数に関する意見陳述"

  - id: "chunk_002_2"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       望ましい定数をどう考えるかとの問いに対し、現在ほどの定数
      がなくても国会は十分に運営できるので定数を削減してもよ
      いと考える旨の回答があった。
    position: "削減容認派（次世代）"
    speaker: "園田博之 議員（次世代の党）"
    context: "質疑応答"

  - id: "chunk_003_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       定数は削減すべきであると考えるが、削減数については、野党
      ５党案に示された小選挙区の定数25削減のＡ案か15削減のＢ
      案のどちらかにすることを考えている。
    position: "削減容認派（生活）"
    speaker: "玉城デニー 議員（生活の党と山本太郎となかまたち）"
    context: "議員定数に関する意見陳述"

  - id: "chunk_003_2"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       定数削減は、議員数が多く無駄があるので効率化のために行う
      のか、今まで行っていたことをやめるとの決心で行うのか、と
      の問いに対し、平成の大合併が進み、市町村の議員数も削減さ
      れている状況に鑑み、国民の要請があれば国会も努力する姿勢
      を示していくべきではないかとの議論があって案を取りまと
      めた経緯がある旨の回答があった。
    position: "削減容認派（生活）"
    speaker: "玉城デニー 議員（生活の党と山本太郎となかまたち）"
    context: "質疑応答"

  - id: "chunk_004_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       当初、定数半減を掲げていたが、定数削減をし過ぎると較差是
      正が難しくなることや、各委員会の割り当て、審議の深掘り、
      さまざまな意見の国政への反映という点からも行き過ぎと考
      えられることから、現在は削減数を示していない。
    position: "定数削減と較差是正の同時検討派（新党改革）"
    speaker: "荒井広幸 議員（新党改革）"
    context: "議員定数に関する意見陳述"

  - id: "chunk_004_2"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       重複立候補は、当初、小選挙区制を導入するために、少数政党の声の吸収や選挙区における候補者調整に有益であるとして導入されたが、内々では、小選挙区で落選しても比例で救済されるという一騎打ちの緩衝的な役割もかなり議論されていたところであり、選挙区で落選して比例で当選するのはわかりづらく、純粋比例ならば理念にかなうのではないか、との旨の回答があった。
    position: "独立議論派（他党派）"
    speaker: "荒井広幸 議員（新党改革）"
    context: "質疑応答（重複立候補について）"

  - id: "chunk_004_3"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       重複立候補制度及び同一順位に候補者を並べて惜敗率で当選
      者を決定する現行の方法についてどのように考えるかとの問
      いに対し、（小選挙区で負けたのに比例で復活するというやり
      方...）それは、根本が小選挙区比例
      代表並立制にあるので、ゆがみを正し、比例代表を中心とした
      選挙制度への転換こそがそれらに答えていく道と考える旨の
      回答があった。
    position: "比例制移行派（共産）"
    speaker: "穀田恵二 議員（日本共産党）"
    context: "質疑応答（重複立候補・復活当選について）"

  - id: "chunk_004_4"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       望ましい定数についての議論は、理想論から出発するのか、現
      実にこれ以上減らすべきではないというところから出発する
      のかとの問いに対し、現実論から出発するが、政治改革のとき
      もあった総定数500名程度というのがよいのか疑問を持つ反面
      （1925年の男子普通選挙実施時の人口12万人に議員１人とい
      う基準で算定した）1200名というのも多すぎるとの意見もある
      旨の回答があった。
    position: "削減反対派（共産、社民）"
    speaker: "穀田恵二 議員（日本共産党）"
    context: "質疑応答（定数の基準について）"

  - id: "chunk_005_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       議員数の削減が国会運営にもたらす問題は具体的にどのよう
      なものかとの問いに対し、議員は常任委員会や特別委員会を３
      つ、４つ兼務し、各委員会が法案審議や一般質疑を行う中で、
      まともに勉強する時間がなくなり質疑の質的低下をもたらす
      というのがメディアにおける批判的な見解であり、 （議員を）
      減らせばよいという言い方はよくないという議論も出ている
      旨の回答があった。
    position: "機能維持・較差是正優先派（共産、社民）"
    speaker: "穀田恵二 議員（日本共産党）"
    context: "質疑応答（議員数削減が国会運営にもたらす問題について）"

  - id: "chunk_005_2"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       議員数の削減が国会運営にもたらす問題は具体的にどのよう
      なものかとの問いに対し、議員は常任委員会や特別委員会を３
      つ、４つ兼務し、各委員会が法案審議や一般質疑を行う中で、
      まともに勉強する時間がなくなり質疑の質的低下をもたらす
      というのがメディアにおける批判的な見解であり、 （議員を）
      減らせばよいという言い方はよくないという議論も出ている
      旨の回答があった。
    position: "機能維持・較差是正優先派（共産、社民）"
    speaker: "穀田恵二 議員（日本共産党）"
    context: "質疑応答（議員数削減が国会運営にもたらす問題について）"

  - id: "chunk_006_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       20年間の「政治改革」を検証する時期であり、定数の問題は
      「政治改革」の時に一緒に議論された政党助成金、企業・団体
      献金の問題とともに検証、議論すべ
      きものであると考える旨の付言があった。
    position: "同時検証派（共産）"
    speaker: "穀田恵二 議員（日本共産党）"
    context: "質疑応答（定数の基準について）"

  - id: "chunk_007_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       比例代表選挙の定数を削減することは容認できない。
    position: "比例制移行派（共産）"
    speaker: "吉川元 議員（社会民主党）"
    context: "議員定数に関する意見陳述"

  - id: "chunk_007_2"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       削減論が多いことについてどう考えるかという問いに対し、国
      民に増税をお願いすることは負担が増えることなのであるか
      ら、それに応じて様々な人の声を国会により反映させるという
      のが民主主義の本来のあり方であると思う旨の回答があった。
    position: "削減反対派（共産、社民）"
    speaker: "吉川元 議員（社会民主党）"
    context: "質疑応答"

  - id: "chunk_008_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       小選挙区定数の削減の基準点はどこか（300 議席か、295 議席
      か） との問いに対し、 現在の295議席であるとの回答があった。
       小選挙区と比例代表の議席数の比率をどのように考えるかと
      の問いに対し、６対４（注：現行制度の創設時の小選挙区300対比例
      代表200の比率）と考える旨の回答があった。
    position: "小選挙区中心削減派（次世代）"
    speaker: "園田博之 議員（次世代の党）"
    context: "質疑応答"

  - id: "chunk_009_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       比例代表定数の削減幅をどのように考えるか、また、小選挙区
      と比例代表の議席の割合をどのように考えるか、との問いに対
      し、当初は衆議院の定数を400（80削減）とし、小選挙区270
      （30削減） 、比例代表130（50削減）としていたが、野党間の
      協議を経て、まず小選挙区の定数を削減することとし、比例代
      表については数字を示さない、小選挙区と比例代表の比率はお
      おむね３対２という形で削減し、削減数にはこだわらない、と
      いうことになったものである旨の回答があった。
    position: "小選挙区中心削減派（生活）"
    speaker: "玉城デニー 議員（生活の党と山本太郎となかまたち）"
    context: "質疑応答"

  - id: "chunk_010_1"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       新たな中選挙区制度への抜本的改正を行う中で、一票の較差是
      正と定数削減をあわせて行うべきものと考えている。
    position: "定数削減と較差是正の同時検討派（新党改革）"
    speaker: "荒井広幸 議員（新党改革）"
    context: "議員定数に関する意見陳述"

  - id: "chunk_010_2"
    source_doc_id: "senkyoseido_08.gijigaiyo.pdf"
    source_filename: "senkyoseido_08.gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_08.gijigaiyo.pdf/$File/senkyoseido_08.gijigaiyo.pdf"
    source_date: "2015-04-08"
    verbatim_quote: |
       中選挙区制の提案に当たり定数をどのように考えているのか
      との問いに対し、 ３人区 （の中選挙区制） をイメージしており、
      定数は30から80程度削減できるのではないかと考えている旨
      の回答があった。
    position: "中選挙区制による削減 ←→ 現行制度維持・比例制移行"
    speaker: "荒井広幸 議員（新党改革）"
    context: "質疑応答"
```

---

## File: senkyoseido_09.gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "定数削減の議論の進め方と合理的な根拠の必要性"
    category: "主要論点"
    summary: "定数削減を実施する場合、各党が提示した数字を踏まえ、シミュレーションを行いながら、どの削減案が最も妥当で実現可能性が高いかを議論すべきである。特に、人口の変化に着目するなど、合理的な根拠に基づいた方法論が求められている。"
    spectrum:
      axis: "各党案の採用 ←→ 合理的根拠に基づく議論"
      positions:
        - label: "各党案の提示"
          description: "各党が提示した削減案の数字を基に議論を進める。"
        - label: "合理的根拠の重視"
          description: "人口の変化など、合理的な根拠に基づいた方法論で削減規模を決定すべき。"
      consensus_status: "継続検討"
      consensus_detail: "定数削減の具体的な規模や方法について、各党の案を参考にしつつも、合理的な根拠に基づいた議論が必要であるという認識が共有されている。"
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_09.gijigaiyo.pdf"
        source_filename: "senkyoseido_09.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_09.pdf/$File/senkyoseido_09.pdf"
        source_date: "2015-05-20"
        verbatim_quote: |
          定数削減については、各党が提示した数字を踏まえ、シミュレーションを行いながら、どのあたりが一番妥当で実現可能性のあるものであるのかというように議論を立てていくのがよいのではないか。
        position: "各党案の提示"
        speaker: "委員"
        context: "定数削減に関する議論の進め方について"
      - id: "chunk_002"
        source_doc_id: "senkyoseido_09.gijigaiyo.pdf"
        source_filename: "senkyoseido_09.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_09.pdf/$File/senkyoseido_09.pdf"
        source_date: "2015-05-20"
        verbatim_quote: |
          今回のヒアリングでは、その内容が必ずしも明確ではないものが多かった。
          どうしても定数削減を行うならば、人口の変化に着目するなど、合理的な根拠で説明できる方法を考える必要があるのではないか。
        position: "合理的根拠の重視"
        speaker: "委員"
        context: "定数削減の議論における根拠の明確化について"

  - id: "topic_002"
    title: "小選挙区定数比率の整合性に関する懸念"
    category: "課題・懸念"
    summary: "自民党案（66.29%）や維新案（71%）における小選挙区定数の比率について、その整合性や妥当性に関する議論が必要とされている。"
    spectrum:
      axis: "自民党案（66.29%） ←→ 維新案（71%）"
      positions:
        - label: "自民党案支持"
          description: "小選挙区定数比率66.29%を支持する立場。"
        - label: "維新案支持"
          description: "小選挙区定数比率71%を支持する立場。"
      consensus_status: "継続検討"
      consensus_detail: "各党案で示された小選挙区定数の比率について、その妥当性や整合性をどう考えるかという点が論点となっている。"
    evidence_chunks:
      - id: "chunk_003"
        source_doc_id: "senkyoseido_09.gijigaiyo.pdf"
        source_filename: "senkyoseido_09.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_09.pdf/$File/senkyoseido_09.pdf"
        source_date: "2015-05-20"
        verbatim_quote: |
          （総定数に占める）小選挙区定数の比率が、自民党案では66.29％（３分の２）、維新案では71％となるが、その整合性についてどう考えるのか。
        position: null
        speaker: "委員"
        context: "各党案の小選挙区定数比率の比較と整合性についての問い"

  - id: "topic_003"
    title: "人口比例方式採用時の将来的な継続性の覚悟"
    category: "課題・懸念"
    summary: "人口比例に基づいて議席を配分する方式を採用する場合、将来にわたってその方式を継続していく覚悟が必要であるという指摘がある。"
    spectrum:
      axis: "人口比例方式の採用 ←→ 継続性の確保"
      positions:
        - label: "人口比例方式採用"
          description: "人口比例に基づく配分方式を採用する。"
        - label: "継続性の確保"
          description: "人口変動に対応し続けることへの覚悟が必要。"
      consensus_status: "継続検討"
      consensus_detail: "人口比例方式の採用は、将来的な人口変動に継続的に対応していくというコミットメントを伴うため、その点を考慮する必要がある。"
    evidence_chunks:
      - id: "chunk_004"
        source_doc_id: "senkyoseido_09.gijigaiyo.pdf"
        source_filename: "senkyoseido_09.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_09.pdf/$File/senkyoseido_09.pdf"
        source_date: "2015-05-20"
        verbatim_quote: |
          人口比例と議席を結びつける方式を採用したら、将来にわたり続ける覚悟が必要である。
        position: null
        speaker: "委員"
        context: "人口比例方式を採用する場合の長期的な視点について"

  - id: "topic_004"
    title: "民主党案における人口50万人当たり定数1の明快さとアダムズ方式的利点"
    category: "主要論点"
    summary: "民主党案が提示する「人口50万人当たりに定数１を人口比例で配分する」という方式は、非常に明快であり、ビルトインされた定数縮減の要素も含まれていると評価されている。これはアダムズ方式的な利点を持つと考えられる。"
    spectrum:
      axis: "民主党案の明快さ ←→ 1人別枠との誤解回避"
      positions:
        - label: "民主党案の評価"
          description: "人口50万人当たり定数1の方式の明快さと定数縮減効果を評価する。"
        - label: "説明の必要性"
          description: "アダムズ方式と1人別枠方式との誤解を避けるための説明が必要。"
      consensus_status: "継続検討"
      consensus_detail: "民主党案の方式の利点（明快さ、定数縮減効果）が認識されている一方で、1人別枠方式との混同を避けるための丁寧な説明が求められている。"
    evidence_chunks:
      - id: "chunk_005"
        source_doc_id: "senkyoseido_09.gijigaiyo.pdf"
        source_filename: "senkyoseido_09.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_09.pdf/$File/senkyoseido_09.pdf"
        source_date: "2015-05-20"
        verbatim_quote: |
          民主党案が、小選挙区について、人口50万人当たりに定数１を人口比例で配分するとしていることは、非常に明快であり、ビルトインされた定数縮減も組み込まれているというふうにも読めるし、住民の側からすれば、100 万人いたら３議席あるが、今度は99 万人になったので議席が１つ減るということを前もって提示しておけばわかりやすく、このあたりはアダムズ方式的な考え方の利点ではないかと思う。
        position: "民主党案の評価"
        speaker: "委員"
        context: "民主党案の人口比例配分方式の評価"
      - id: "chunk_006"
        source_doc_id: "senkyoseido_09.gijigaiyo.pdf"
        source_filename: "senkyoseido_09.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_09.pdf/$File/senkyoseido_09.pdf"
        source_date: "2015-05-20"
        verbatim_quote: |
          各党の意見を聞くと、アダムズ方式は、あまり違和感なく浸透し始めてい
るように思われるが、１人別枠との誤解を受けないよう、本質的な意
味合いを明らかにして説明を行う必要がある。
        position: "説明の必要性"
        speaker: "委員"
        context: "アダムズ方式と1人別枠方式の混同回避について"
```

---

## File: senkyoseido_10.gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "定数削減に伴う人口減少地域の議席減少と一票の較差是正の困難化"
    category: "課題・懸念"
    summary: "人口減少に伴い定数を削減した場合、人口減少地域の議席がさらに減少し、結果として一票の較差是正がより困難になるのではないかという懸念が示された。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_10.gijigaiyo.pdf"
        source_filename: "senkyoseido_10.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_10.gijigaiyo.pdf/$File/senkyoseido_10.gijigaiyo.pdf"
        source_date: "2015-06-15"
        verbatim_quote: |
           人口減に伴って定数を減らすこととした場合、 人口減少地域の少ない議席
          がまた減ることになり、一票の較差是正も一層困難になるのではないか。
        position: null
        speaker: "各委員"
        context: "民主党案、維新案関連の議論"

  - id: "topic_002"
    title: "定数削減の許容範囲と立法府機能の維持"
    category: "主要論点"
    summary: "定数削減を実施するにあたり、立法府としての機能を維持できる限界点がどこにあるのかを検討する必要があるという指摘があった。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_002"
        source_doc_id: "senkyoseido_10.gijigaiyo.pdf"
        source_filename: "senkyoseido_10.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_10.gijigaiyo.pdf/$File/senkyoseido_10.gijigaiyo.pdf"
        source_date: "2015-06-15"
        verbatim_quote: |
           定数削減については、 立法府としての機能を維持しながらどの程度まで削
          減できるのかを検討する必要がある。
        position: null
        speaker: "各委員"
        context: "民主党案、維新案関連の議論"

  - id: "topic_003"
    title: "議員一人当たりの人口基準の妥当性"
    category: "課題・懸念"
    summary: "議員一人当たりの人口を50万人とする基準が妥当かどうか、諸外国との比較を踏まえて検討すべきであるという意見が出された。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_003"
        source_doc_id: "senkyoseido_10.gijigaiyo.pdf"
        source_filename: "senkyoseido_10.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_10.gijigaiyo.pdf/$File/senkyoseido_10.gijigaiyo.pdf"
        source_date: "2015-06-15"
        verbatim_quote: |
           日本の国会議員数は諸外国に比べて決して多くはなく、 （議員１人当たり
          50万人という数字でよいのか。
        position: null
        speaker: "各委員"
        context: "民主党案、維新案関連の議論"

  - id: "topic_004"
    title: "将来の人口推計に基づく定数配分の検討"
    category: "主要論点"
    summary: "将来の人口推計（平成32年、平成42年）に基づき、人口変動を考慮した定数の変化を試算した結果が示され、議論の基礎とされた。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_004"
        source_doc_id: "senkyoseido_10.gijigaiyo.pdf"
        source_filename: "senkyoseido_10.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_10.gijigaiyo.pdf/$File/senkyoseido_10.gijigaiyo.pdf"
        source_date: "2015-06-15"
        verbatim_quote: |
           「人口の変動と議席」について
          平成32年推計人口、平成42年推計人口の平成22年国調人口からの
          人口減少率を適用した場合の定数の変化の試算の結果について説明が
          あった。
        position: null
        speaker: "事務局"
        context: "議題「小選挙区比例代表並立制の検証」における事務局説明"

  - id: "topic_005"
    title: "将来の定数決定のタイミングに関する意見"
    category: "課題・懸念"
    summary: "現段階で将来の定数（将来の人口推計に基づくもの）まで決定することの是非について疑問が呈された。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_005"
        source_doc_id: "senkyoseido_10.gijigaiyo.pdf"
        source_filename: "senkyoseido_10.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_10.gijigaiyo.pdf/$File/senkyoseido_10.gijigaiyo.pdf"
        source_date: "2015-06-15"
        verbatim_quote: |
           現段階で将来の定数まで決めるのはいかがなものか。
        position: null
        speaker: "各委員"
        context: "民主党案、維新案関連の議論"

  - id: "topic_006"
    title: "維新の党案による総定数削減の具体的内容"
    category: "主要論点"
    summary: "維新の党から提示された、総定数を3割削減する2つの案（①案：小選挙区240/比例180→96、②案：小選挙区210/比例126）が試算の基礎として提示された。"
    spectrum:
      axis: "案①（小240/比例96） ←→ 案②（小210/比例126）"
      positions:
        - label: "案①支持"
          description: "小選挙区240、比例代表96の定数配分案"
        - label: "案②支持"
          description: "小選挙区210、比例代表126の定数配分案"
      consensus_status: "継続検討"
      consensus_detail: "具体的な削減案が提示されたが、採用には至っていない。"
    evidence_chunks:
      - id: "chunk_006"
        source_doc_id: "senkyoseido_10.gijigaiyo.pdf"
        source_filename: "senkyoseido_10.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_10.gijigaiyo.pdf/$File/senkyoseido_10.gijigaiyo.pdf"
        source_date: "2015-06-15"
        verbatim_quote: |
           「維新案の比例代表定数による各党の獲得議席数の試算」について
          維新の党から提示された総定数を３割削減する２つの案（①案小選挙
          区定数240比例代表定数96、②案小選挙区定数210比例代表定数126）
          に基づき、 比例代表選挙の各党の議席数及び各ブロックの定数を試算し
          た結果について説明があった。
        position: null
        speaker: "事務局"
        context: "議題「小選挙区比例代表並立制の検証」における事務局説明"

  - id: "topic_007"
    title: "小選挙区の選挙可能人口規模の議論の必要性"
    category: "主要論点"
    summary: "定数削減や人口変動を議論する上で、選挙が行える最小の選挙区人口規模に関する議論が必要であるとの指摘があった。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_007"
        source_doc_id: "senkyoseido_10.gijigaiyo.pdf"
        source_filename: "senkyoseido_10.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_10.gijigaiyo.pdf/$File/senkyoseido_10.gijigaiyo.pdf"
        source_date: "2015-06-15"
        verbatim_quote: |
           小選挙区については、 選挙が行える１選挙区の人口規模の観点からの議論
          も行う必要がある。
        position: null
        speaker: "各委員"
        context: "民主党案、維新案関連の議論"
```

---

## File: senkyoseido_11.gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "議員定数削減が議会の機能に与える影響"
    category: "課題・懸念"
    summary: "議員定数を削減しすぎると、憲法が議会に要請する職務を遂行できなくなるおそれがあるという懸念が示された。定数削減は効率化という一面だけでなく、クオリティーと適正な民意の集約という両面から検討すべきである。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_11"
        source_filename: "senkyoseido_11.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_11.gijigaiyo.pdf/$File/senkyoseido_11.gijigaiyo.pdf"
        source_date: "2015-07-13"
        verbatim_quote: |
          議員は数とクオリティーの双方が必要である。 議員定数の削減は効率化であり国民にとってよいことであるというのは一面的であり、 削減し過ぎると憲法が議会に要請する仕事ができなくなるおそれがある。 クオリティーと適正な民意の集約という両面から考えていくべきではないか。
        position: null
        speaker: "調査会における議論"
        context: "選挙制度に関する議論の中で、議員定数削減の是非について言及された点。"

  - id: "topic_002"
    title: "比例代表定数削減による民意集約機能への影響"
    category: "課題・懸念"
    summary: "比例代表の定数が削減された結果、民意の集約機能が強くなりすぎているのではないかという指摘があった。これは、定数削減の方向性が民意の反映に与える影響に関する懸念である。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_002"
        source_doc_id: "senkyoseido_11"
        source_filename: "senkyoseido_11.gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_11.gijigaiyo.pdf/$File/senkyoseido_11.gijigaiyo.pdf"
        source_date: "2015-07-13"
        verbatim_quote: |
          選挙制度全体として比例代表の定数が削減されたことにより民意の集約機能が強くなってしまっているのではないか。
        position: null
        speaker: "調査会における議論"
        context: "選挙制度全体に関する議論の中で、比例代表定数削減の影響について指摘された点。"
```

---

## File: senkyoseido_12gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "定数削減の必要性と合理的な理由付け"
    category: "主要論点"
    summary: "定数削減の是非、および削減する場合の合理的な理由付け（特に人口減少を理由とすることの是非）について議論されている。"
    spectrum:
      axis: "人口減少を主たる理由とすべきか ←→ 他の理由や代替案を検討すべきか"
      positions:
        - label: "人口減少を合理的な理由とする立場"
          description: "人口減少を理由とする定数削減は最も合理的な理由であると考える立場。"
        - label: "人口基準の難しさや代替案を指摘する立場"
          description: "議席数は人口とリンクしているわけではなく、国会機能や過去の実績を踏まえて検討すべきであり、人口を基準にすることは難しいとする立場。また、身を切る約束であればコスト削減など他の方法もあるとする指摘。"
      consensus_status: "継続検討"
      consensus_detail: "人口減少を理由とする妥当性について意見が分かれており、定数削減の根拠をどう設定するかが論点となっている。"
    evidence_chunks:
      - id: "chunk_001_a"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          定数削減をするのであれば合理的な理由が必要であり、それ
          を人口減少
          に求めることはできるが、人口減少をビルトインするわけではなく、今
          回の定数削減に関しては（人口減少が）最も合理的な理由であると考え
          ればよいのではないか。
        position: "人口減少を主たる理由とすべきか"
        speaker: "委員（特定不可）"
        context: "定数削減の理由付けに関する議論"
      - id: "chunk_001_b"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          身を切ることが国民との約束であるとすれば、定数削減ではなく、例え
          ばコスト削減など他の方法もある。
        position: "人口減少を主たる理由とすべきか"
        speaker: "委員（特定不可）"
        context: "定数削減の代替案に関する指摘"
      - id: "chunk_001_c"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          議席数はその時々の政治的情勢や社会的情勢で決まり、 日本も300から
          スタートして以来変動してきており、また、世界各国でもばらばらであ
          り、必ずしも人口とリンクしているわけではないので、人口を基準にす
          ることは難しいのではないか。もし削減するのであれば、過去の我が国
          の実績などを踏まえて議員数を検討すればよいのではないか。
        position: "人口基準の難しさや代替案を指摘する立場"
        speaker: "委員（特定不可）"
        context: "人口を基準とすることの難しさに関する指摘"

  - id: "topic_002"
    title: "定数削減と一票の較差是正の矛盾"
    category: "課題・懸念"
    summary: "定数削減は、一票の較差是正という目標と矛盾する目標であるため、有識者としてその点を国民に明確に提示する必要があるという指摘。"
    spectrum:
      axis: "矛盾の提示の必要性"
      positions:
        - label: "矛盾を明確に提示すべき立場"
          description: "一票の較差是正と定数削減が矛盾する目標であることを有識者の立場から明確に示すべきとする立場。"
        - label: "特になし（合意事項の可能性）"
          description: ""
      consensus_status: "継続検討"
      consensus_detail: "定数削減を進める場合、一票の較差是正とのトレードオフをどう扱うかが課題。"
    evidence_chunks:
      - id: "chunk_002_a"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          国民に、小選挙区の議席配分において、一票の較差是正と定数削減は矛
          盾する目標であることを有識者の立場から明確に提示する必要がある。
        position: "矛盾を明確に提示すべき立場"
        speaker: "委員（特定不可）"
        context: "定数削減と一票の較差是正の関係性に関する指摘"

  - id: "topic_003"
    title: "定数削減の適切な水準の決定基準"
    category: "主要論点"
    summary: "国会が適切に機能するために必要な議員数、および国民の声を吸い上げるために議員一人当たりの人口がどの程度が適正かという観点から、削減の是非と水準を議論すべきという意見。"
    spectrum:
      axis: "機能維持のための必要数 ←→ 削減の是非"
      positions:
        - label: "機能維持を重視する立場"
          description: "国会がきちんと機能し、国民の選ぶ権利を担保できる水準を議論した上で定数削減を考えるべきとする立場。"
        - label: "削減を強く主張する立場"
          description: "身を切る改革として議論を最後にすべきであり、削減を避けるべきではないとする立場。"
      consensus_status: "継続検討"
      consensus_detail: "国会機能の維持と削減のバランスをどう取るかが論点。"
    evidence_chunks:
      - id: "chunk_003_a"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          どの程度の国会議員数で国会がきちんと機能するか、 選挙の形で国民の
          声を吸い上げるのに国会議員1人当たり人口はどの程度が適正かという
          ことを議論した上で定数削減を考えるべきである。
        position: "機能維持を重視する立場"
        speaker: "委員（特定不可）"
        context: "定数削減の議論の前提となるべき基準に関する指摘"
      - id: "chunk_003_b"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          議席数はその時々の政治的情勢や社会的情勢で決まり、 日本も300から
          スタートして以来変動してきており、また、世界各国でもばらばらであ
          り、必ずしも人口とリンクしているわけではないので、人口を基準にす
          ることは難しいのではないか。
        position: "機能維持を重視する立場"
        speaker: "委員（特定不可）"
        context: "定数決定の歴史的・国際的背景に関する指摘"

  - id: "topic_004"
    title: "定数削減の実施箇所（小選挙区 vs 比例代表）"
    category: "主要論点"
    summary: "定数削減を行う場合、小選挙区と比例代表のどちらを削減すべきかについて意見が分かれている。小選挙区の弊害是正の観点や、比例代表のバッファー機能の維持の観点から議論されている。"
    spectrum:
      axis: "小選挙区削減 ←→ 比例代表削減"
      positions:
        - label: "小選挙区削減派"
          description: "現在の選挙結果の振幅が激しいのは小選挙区の力が強いためであり、削減するなら小選挙区で行うべきとする立場。"
        - label: "比例代表削減派"
          description: "拘束名簿式への不信や、離党・新党設立の問題から、比例代表の定数を削減すべきとする立場。"
      consensus_status: "継続検討"
      consensus_detail: "削減の対象をどこにするかについて明確な合意に至っていない。"
    evidence_chunks:
      - id: "chunk_004_a"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          小選挙区制の弊害の問題を少しでも是正するという意味でいうと、小選
          挙区の方を少し調整していった方が適切な民意の反映ということに寄
          与するのではないか。
        position: "小選挙区削減派"
        speaker: "委員（特定不可）"
        context: "小選挙区制の弊害是正の観点からの削減提案"
      - id: "chunk_004_b"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          拘束名簿で選ばれながら選挙後に離党や新党設立があったり、 有権者に
          とっては一番候補者が選べない拘束名簿式という投票方法であったり、
          重複立候補制度など、比例代表への国民の不信がある。選挙区の安定性
          を重視するためにも、比例代表の定数を削減すべきである。
        position: "比例代表削減派"
        speaker: "委員（特定不可）"
        context: "比例代表への不信感に基づく削減提案"
      - id: "chunk_004_c"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          現在の選挙結果を見ると、振幅が激しくなり、小選挙区の持つ力が非常
          に発揮されて第１党が多数の議席を占める状況になっている。 そういう
          中で、定数削減を考える場合は、小選挙区で削減すべきである。
        position: "小選挙区削減派"
        speaker: "委員（特定不可）"
        context: "小選挙区の過度な影響を是正する観点からの削減提案"

  - id: "topic_005"
    title: "定数削減が議会機能と行政府との関係に与える影響"
    category: "課題・懸念"
    summary: "議院内閣制のもとで、行政府に対抗する議会の力が弱まることへの懸念。また、有為な人材を集めるためにはある程度の議席数が必要であるという指摘。"
    spectrum:
      axis: "議会機能維持のための必要数維持 ←→ 削減推進"
      positions:
        - label: "議会機能維持を重視する立場"
          description: "議会が減少しすぎると行政府との対抗関係上好ましくなく、有為な人材確保のためにもある程度の数が必要であるとする立場。"
        - label: "削減を容認する立場"
          description: ""
      consensus_status: "継続検討"
      consensus_detail: "定数削減が議会権能に与える影響を考慮する必要がある。"
    evidence_chunks:
      - id: "chunk_005_a"
        source_doc_id: "senkyoseido_12gijigaiyo.pdf"
        source_filename: "senkyoseido_12gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_12gijigaiyo.pdf/$File/senkyoseido_12gijigaiyo.pdf"
        source_date: "2015-09-30"
        verbatim_quote: |
          議院内閣制のもとでの行政府との対抗関係上、 あまり議会の方が減るこ
          とは好ましくない。 有為な人材を集めるためにはある程度幅を持って人
          数がいた方がよいので、 議会と行政府の関係を考えることも重要である。
        position: "議会機能維持を重視する立場"
        speaker: "委員（特定不可）"
        context: "議会と行政府の関係性から見た定数削減への懸念"
```

---

## File: senkyoseido_13gijigaiyo.pdf

ご提示いただいたドキュメント（senkyoseido_13gijigaiyo.pdf）を分析した結果、「議員定数削減」に直接関連する論点は、**この議事概要内では明確に抽出できませんでした**。

この資料（第13回 衆議院選挙制度に関する調査会 議事概要）の主な議論の焦点は以下の2点に絞られています。

1.  **一票の較差（特に都道府県への定数配分）**：最高裁判決への対応、選挙区割りの見直し方法。
2.  **比例代表制度**：当選者の決定方式、ブロック規模の検討。

「議員定数削減」そのものに関する具体的な議論や、削減を前提とした設計上の論点（例：削減目標、削減方法の配分、削減による影響の懸念など）についての言及は、この議事録の範囲内では確認できませんでした。

ただし、**比例代表の当選者決定方式の議論**の中で、**定数削減**が仮定された場合の議論が触れられています。これを「議員定数削減」の設計論点として抽出します。

---

```yaml
topics:
  - id: "topic_001"
    title: "比例代表における定数削減と当選者決定方式の連動"
    category: "課題・懸念"
    summary: "もし将来的に定数削減を比例代表で行う場合、小選挙区制における過剰代表的性格を考慮し、当選者の決定方式（例：名簿順位など）をセットで検討する必要があるという指摘があった。"
    
    spectrum: null

evidence_chunks:
  - id: "chunk_001"
    source_doc_id: "senkyoseido_13gijigaiyo.pdf"
    source_filename: "senkyoseido_13gijigaiyo.pdf"
    source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_13gijigaiyo.pdf/$File/senkyoseido_13gijigaiyo.pdf"
    source_date: "平成27年10月19日"
    verbatim_quote: |
      仮に定数削減を比例代表で行うとすれば、 小選挙区制における過剰代表
      的性格を考慮して、 当選者の決定方式を検討することも必要であるので、
      総数の問題と（当選者の）決定方法の問題は、分離せずにセットで議論
      した方が現実に妥当する。
    position: null
    speaker: "（委員）"
    context: "比例代表の議論の中で、定数削減が仮定された場合の設計論点として言及。"
```

---

## File: senkyoseido_14gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "定数削減の具体的な削減数と総定数の決定方法"
    category: "主要論点"
    summary: "議員定数削減の議論において、削減の「数」をどう決めるか、また削減後の「総定数」をどう設定するかという視点からの検討が必要であるという指摘があった。"
    spectrum:
      axis: "削減数決定の焦点"
      positions:
        - label: "削減数（差分）に着目"
          description: "削減数をどれくらいにするかという点に焦点を当てるべき。"
        - label: "削減後の総定数に着目"
          description: "削減後の総定数が何人になるのかという面から考えるべき。"
      consensus_status: "継続検討"
      consensus_detail: "削減の具体的な目標値（削減数か総定数か）について、議論の視点を定める必要がある。"
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_14gijigaiyo.pdf"
        source_filename: "senkyoseido_14gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_14gijigaiyo.pdf/$File/senkyoseido_14gijigaiyo.pdf"
        source_date: "2015-11-19"
        verbatim_quote: |
           定数削減については、 削減数をどれくらいにするかということもあるが、
          削減後の総定数が何人になるのかという面から考えることも必要ではないか。
        position: "削減後の総定数に着目"
        speaker: "各委員"
        context: "議員定数削減に関する議論の中で、削減の目標設定の視点について言及。"

  - id: "topic_002"
    title: "選挙制度改革の議論の包括性（一票の較差是正と総合的視点）"
    category: "課題・懸念"
    summary: "有権者は単なる一票の較差是正といった緊急的なテーマだけでなく、選挙制度全体の総合的な姿を見据えた議論を期待している。これは、定数削減を含む制度改革が、より広範な代表性の問題と関連づけられていることを示唆する。"
    spectrum:
      axis: "議論の範囲"
      positions:
        - label: "緊急的テーマ（一票の較差是正）"
          description: "一票の較差是正を主眼とする。"
        - label: "総合的テーマ（全体像）"
          description: "一票の較差是正だけでなく、制度全体の姿を見据えるべき。"
      consensus_status: "両論併記"
      consensus_detail: "一票の較差是正は重要だが、有権者はそれ以上の総合的な改革を求めているという認識が共有されている。"
    evidence_chunks:
      - id: "chunk_002"
        source_doc_id: "senkyoseido_14gijigaiyo.pdf"
        source_filename: "senkyoseido_14gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_14gijigaiyo.pdf/$File/senkyoseido_14gijigaiyo.pdf"
        source_date: "2015-11-19"
        verbatim_quote: |
           本調査会では、一票の較差是正などの緊急的なテーマのみではなく、総
          合的に問題を捉え、全体的な姿を見据えて議論がなされることを有権者
          は期待している。
        position: "総合的テーマ（全体像）"
        speaker: "各委員"
        context: "有権者の期待に関する発言として、議論の範囲の広さの必要性が指摘された。"

  - id: "topic_003"
    title: "人口変動を前提とした選挙区の変更の前提"
    category: "主要論点"
    summary: "現行制度の根幹は人口変動に応じて議席を動かすことであり、人口変動があれば選挙区が変化することは前提であるという認識が示された。これは、定数削減の議論と並行して、選挙区の再編が不可避であることを示唆している。"
    spectrum:
      axis: "選挙区変更の頻度と前提"
      positions:
        - label: "人口変動による変更は前提"
          description: "人口変動がある限り、選挙区の変更は制度の根幹として発生する。"
        - label: "人口変動以外の要因も考慮すべき"
          description: "（本ドキュメント内では明確な対立意見なし）"
      consensus_status: "継続検討"
      consensus_detail: "人口変動を前提とする現行制度の構造が、定数削減や一票の較差是正の議論の背景にある。"
    evidence_chunks:
      - id: "chunk_003"
        source_doc_id: "senkyoseido_14gijigaiyo.pdf"
        source_filename: "senkyoseido_14gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_14gijigaiyo.pdf/$File/senkyoseido_14gijigaiyo.pdf"
        source_date: "2015-11-19"
        verbatim_quote: |
           現行制度の根幹は、人口の変動によって議席を動かすことであり、人口
          の変動があった場合には、選挙区が変化することがあるという前提があ
          る。
        position: "人口変動による変更は前提"
        speaker: "各委員"
        context: "現行制度の基本的な構造についての認識の共有。"
```

---

## File: senkyoseido_15gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "定数削減の必要性と実施時期"
    category: "主要論点"
    summary: "最高裁判決への対応として、定数削減をどの程度優先し、実施すべきかについて、各党で意見が分かれている。"
    spectrum:
      axis: "較差是正先行（定数削減は後回し） ←→ 定数削減と較差是正を同時に実施"
      positions:
        - label: "較差是正優先"
          description: "最高裁の違憲状態判決を踏まえ、一票の較差是正を最優先すべきであり、定数削減は次善の課題とする立場。"
        - label: "定数削減と同時実施"
          description: "定数削減は行政コスト削減の観点からも重要であり、較差是正と同時に実現すべきとする立場。"
      consensus_status: "継続検討"
      consensus_detail: "公明党は較差是正を先行しつつ定数削減も議論を進める姿勢。日本共産党は定数削減に反対し、小選挙区制廃止を主張。"

    evidence_chunks:
      - id: "chunk_001_01"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           調査会では、各都道府県への定数配分にアダムズ方式の導入
          を検討していると承知するが、アダムズ方式の持つ特性に鑑
          みると、現行制度よりも都道府県の人口の比率をより的確に
          反映しやすくなることに加え、選挙区数の変動を少なく抑え
          られ、人口が少ない県でも２選挙区を確保できる可能性が高
          いことなどから検討に値する方式であると考える。
           定数削減について、でき得るならば衆議院選挙制度の抜本改
          革の中で実現すべきと考えるが、当面の課題として定数削減
          を先行するならば、現行制度を基本として、定数削減を検討
          することもやむを得ないと考えている。
        position: "較差是正優先"
        speaker: "北側一雄議員（公明党）"
        context: "定数削減の議論の位置づけについて。"
      - id: "chunk_001_02"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           公明党として定数削減問題をどのように整理しているのかと
          の問いに対し、定数削減についての３党（自民党、民主党、
          公明党）合意もあり、やらなければならないと考えているも
          のの、政党間での合意形成が容易でなかったという経過もあ
          る中で、最高裁の３度の違憲状態判決に対して、一票の較差
          是正を早急に行わなければならないことなので、定数削減を
          しなくてよいということではなく、当然議論を進めていく必
          要があると考えるが、他方、一票の較差是正を先行すること
          もあり得ると考える旨の回答があった。
        position: "較差是正優先"
        speaker: "北側一雄議員（公明党）"
        context: "定数削減と較差是正の優先順位について。"
      - id: "chunk_001_03"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           国民の意見を議会に反映させるツールである議員の削減は、
          国会の声を切り捨てるもの。国会の役割で最も重要なことは、
          政府を監視し、暴走させないようにすることである。定数削
          減が、国会の政府監視機能を低下させることは明らかであり、
          また、我が国の国会議員総定数は、議会制民主主義の発展
          のため、国民代表の在り方について国民的議論をする機会と
          すべきであるが、定数削減の議論がこの点から出発していな
          い。
        position: "定数削減と同時実施"
        speaker: "穀田恵二議員（日本共産党）"
        context: "定数削減に対する反対意見（監視機能低下の懸念）。"
      - id: "chunk_001_04"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           我が党は、一票の較差という問題と同時に、小選挙区制度に
          よる民意と議席数の乖離、すなわち民意の過度な集中によっ
          て生じる膨大な死票の存在も問題視してきた。一票の較差
          是正と民意の反映という二つの課題を同時に実現させるには、
          比例代表制を中心とする選挙制度こそ求められていると考え
          る。
        position: "定数削減と同時実施"
        speaker: "吉川元議員（社会民主党）"
        context: "較差是正と民意の反映を同時に実現するため、比例代表制を中心とする制度を主張。"

  - id: "topic_002"
    title: "定数削減の対象と配分比率"
    category: "主要論点"
    summary: "定数削減を実施する場合、小選挙区と比例代表のどちらを削減するか、また削減後の比率をどう設定するかについて、具体的な提案と対立がある。"
    spectrum:
      axis: "小選挙区削減中心 ←→ 比例代表削減中心"
      positions:
        - label: "小選挙区削減重視"
          description: "小選挙区の民意集約機能が行き過ぎているため、小選挙区の定数を削減すべきとする立場。"
        - label: "比例代表削減重視（自公案）"
          description: "比例代表を削減し、小選挙区定数は維持することで、第1党以外の政党への影響を抑えつつ定数削減を実現する立場。"
      consensus_status: "両論併記"
      consensus_detail: "自民党・公明党は比例30削減で合意。民主党・維新の党は小選挙区削減を主張。公明党は小選挙区削減を主張。"

    evidence_chunks:
      - id: "chunk_002_01"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           定数削減については、調査会の答申を尊重しつつ、各党
          間で再調整を行い、成案を得るものとする。自民・公明
          両党では比例定数30削減を合意している。
        position: "比例代表削減重視（自公案）"
        speaker: "細田博之議員（自由民主党）"
        context: "自民党の定数削減案（比例30削減）。"
      - id: "chunk_002_02"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           我が党は既に、小選挙区240、比例代表96 とする法案を提出
          している。これは消費税の増税が決まった平成24 年当時の定
          数 480 から３割削減するものである。なお、少数政党にも一
          定の議席が得られるようにするために、小選挙区、比例代表
          ともに３割ずつ削減した小選挙区210、比例代表126という考
          え方も選択肢にはある。
        position: "小選挙区削減重視"
        speaker: "松野頼久議員（維新の党）"
        context: "維新の党の定数削減案（全体で3割削減、小選挙区中心の案も提示）。"
      - id: "chunk_002_03"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           現行の小選挙区比例代表並立制は、民意の反映と民意の集約
          の２つの理念を、小選挙区が３、比例代表が２の割合でバラ
          ンスを取ることを趣旨とした制度であるが、現状では、得票
          率と獲得議席数に大きな乖離が生じている。小選挙区の行き
          過ぎた民意の集約機能を是正し、より民意の反映を重視した
          制度に見直す必要があると考えるので、単純に比例代表の定
          数を削減することは認められないと考える。
        position: "小選挙区削減重視"
        speaker: "北側一雄議員（公明党）"
        context: "比例代表削減への反対理由（民意の反映の観点から）。"
      - id: "chunk_002_04"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           小選挙区定数は現行の295とし、比例代表定数のみを30 削減
          した場合、小選挙区と比例代表の定数の比率が２対１になる
          ことをどのように考えるのかとの問いに対し、比例代表で削
          減すると第１党以外の政党に大きな影響が出るため、第２党
          以下の政党が定数削減によっても議席が減らないように第１
          比例枠と第２比例枠を設け、第１党のみが議席を減らし、そ
          れ以外の政党には議席の変動がないようにしている旨の回答
        position: "比例代表削減重視（自公案）"
        speaker: "細田博之議員（自由民主党）"
        context: "比例代表削減案の設計意図（第1党のみが議席減となるように配慮）。"

  - id: "topic_003"
    title: "定数削減の根拠と行政コスト削減の関連性"
    category: "課題・懸念"
    summary: "定数削減を主張する側は行政コスト削減を根拠とするが、削減により国会の政府監視機能が低下する懸念が指摘されている。"
    spectrum:
      axis: "コスト削減優先（議員数削減） ←→ 監視機能維持優先（議員数維持）"
      positions:
        - label: "コスト削減派"
          description: "人口減少と財政状況から、身を切る改革として議員定数削減が必要であるとする立場。"
        - label: "監視機能低下懸念派"
          description: "定数削減は政府監視機能を低下させ、民主主義の根幹を損なうため不当であるとする立場。"
      consensus_status: "両論併記"
      consensus_detail: "維新の党はコスト削減を理由に削減を主張。日本共産党は監視機能低下を理由に削減に反対。"

    evidence_chunks:
      - id: "chunk_003_01"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           議員の数それ自体を削減する理由は何かとの問いに対し、
          我々が主張する道州制の導入も、まず行政コストを下げると
          いう意味が含まれており、現在の人口減少、国の財政を考え
          ると、行政コストを徹底して下げる必要があり、そのための
          第１歩が身を切る改革であると以前より選挙で訴えて議席を
          得ている旨の回答があった。
        position: "コスト削減派"
        speaker: "松野頼久議員（維新の党）"
        context: "定数削減を「身を切る改革」として行政コスト削減の観点から主張。"
      - id: "chunk_003_02"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           国民の意見を議会に反映させるツールである議員の削減は、
          国会の声を切り捨てるもの。国会の役割で最も重要なことは、
          政府を監視し、暴走させないようにすることである。定数削
          減が、国会の政府監視機能を低下させることは明らかであり、
          また、我が国の国会議員総定数は、議会制民主主義の発展
          のため、国民代表の在り方について国民的議論をする機会と
          すべきであるが、定数削減の議論がこの点から出発していな
          い。
        position: "監視機能低下懸念派"
        speaker: "穀田恵二議員（日本共産党）"
        context: "定数削減が政府監視機能を低下させることへの懸念。"

  - id: "topic_004"
    title: "較差是正のための区割り見直しの頻度"
    category: "主要論点"
    summary: "一票の較差を安定的に2倍未満に抑えるため、国勢調査に基づく区割り見直しの頻度を現行の10年から5年ごとに変更すべきかどうかが議論されている。"
    spectrum:
      axis: "現行10年ごと維持 ←→ 5年ごとの義務化"
      positions:
        - label: "5年ごとへの変更を主張"
          description: "人口変動に対応するため、区画審設置法を改正し、見直しを10年から5年ごとに変更すべきとする提案。"
        - label: "現状維持または柔軟な対応"
          description: "具体的な頻度変更の提案はあったが、合意には至っていない。"
      consensus_status: "継続検討"
      consensus_detail: "自民党、生活の党と山本太郎となかまたちが5年ごとの見直しを具体的に提案している。"

    evidence_chunks:
      - id: "chunk_004_01"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           今後５年ごとの国勢調査のたびに区画審で見直しを行い、
          また、２倍未満とするだけでは、すぐに２倍超となりか
          ねないので、見直し後５年間は、人口の増減の趨勢から
          見て２倍を超えないように措置することを法律上規定した
          らどうか。
        position: "5年ごとへの変更を主張"
        speaker: "細田博之議員（自由民主党）"
        context: "較差是正の継続性を担保するための5年ごとの見直し提案。"
      - id: "chunk_004_02"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           区画審設置法を改正して、（区割りの改定作業を）10 年
          ごとから５年ごとに変えるとともに、５年間を考えて２倍を
          超えないよう（原則として、1.95 倍を最大較差とする）措置
          することを法律上規定した方がよいという具体的提案を行っ
          ている旨の回答があった。
        position: "5年ごとへの変更を主張"
        speaker: "細田博之議員（自由民主党）"
        context: "区画審設置法改正による5年ごとの見直し提案の具体化。"
      - id: "chunk_004_03"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           区割り改定案の作成に当たっては、各選挙区間の
          人口較差が２倍以上とならないようにしなければならない、
          各都道府県における小選挙区の数は人口に比例して各都道府
          県に配当した数とする、区画審は５年ごとに行われる国勢調
          査に基づいて改定案を作成し勧告するものとする、政府は区
          画審から勧告があったときは速やかに必要な法制上の措置を
          講ずるものとする、という内容の区画審設置法改正案をとり
          まとめており、これは平成26 年２月の野党５党案に反映され
          ている。
        position: "5年ごとへの変更を主張"
        speaker: "玉城デニー議員（生活の党と山本太郎となかまたち）"
        context: "野党5党案にも5年ごとの見直しが含まれていることの表明。"

  - id: "topic_005"
    title: "定数削減と政党交付金削減の比較"
    category: "課題・懸念"
    summary: "議員歳費の削減と政党交付金の削減のどちらがより効果的か、あるいは適切かについて意見が交わされた。"
    spectrum:
      axis: "歳費削減（議員直接） ←→ 政党交付金削減（間接的）"
      positions:
        - label: "歳費削減を主張"
          description: "議員に直接支給され使い道が自由な歳費を削減すべきであり、政党交付金削減は政治活動の保障との兼ね合いがあるとする立場。"
        - label: "政党交付金削減の可能性"
          description: "定数削減よりも政党交付金を減額した方がコスト削減になるのではないかという問いかけ。"
      consensus_status: "継続検討"
      consensus_detail: "維新の党は歳費削減を主張し、政党交付金削減との比較を行った。"

    evidence_chunks:
      - id: "chunk_005_01"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           （定数削減よりも）政党交付金を減額した方が、コストの削
          減ができるのではないかとの問いに対し、実は政党交付金は、
          パンフレットに要する費用や人件費など政党の政治活動に使
          途が制限されているのが現実なので、正当な政治活動は保障
          しつつ、（定数削減とともに）議員に直接支給され使い道が
          自由な歳費を削減すべきだという考え方である旨の回答があ
          った。
        position: "歳費削減を主張"
        speaker: "松野頼久議員（維新の党）"
        context: "定数削減（歳費削減）と政党交付金削減の比較。"

  - id: "topic_006"
    title: "定数削減と道州制・参議院定数との関連"
    category: "その他"
    summary: "定数削減の議論が、統治機構改革（道州制導入）や参議院定数削減、一院制導入といったより広範な改革と関連づけられている。"
    spectrum:
      axis: "衆議院単独の削減 ←→ 統治機構改革と一体での削減"
      positions:
        - label: "統治機構改革と一体化"
          description: "道州制導入を見据え、選挙制度改革を統治機構改革の一環として議論すべきとする立場。"
        - label: "参議院・一院制の議論"
          description: "衆議院だけでなく参議院も含めた議員定数削減、究極的には一院制導入を視野に入れるべきとする立場。"
      consensus_status: "両論併記"
      consensus_detail: "維新の党が道州制と関連づけ、また参議院も含めた削減を主張。"

    evidence_chunks:
      - id: "chunk_006_01"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           小選挙区制を維持し、選挙区割りを合理的なものとするためには、現在よりも広い広域自治体、道州を設ける必要があり、道州制を見据えた選挙制度を構築し、選挙制度改革も統治機構改革の一環として道州制の議論とあわせて行うべきものと考えている。
        position: "統治機構改革と一体化"
        speaker: "松野頼久議員（維新の党）"
        context: "定数削減を含む選挙制度改革を道州制議論と並行して行うべきとの主張。"
      - id: "chunk_006_02"
        source_doc_id: "senkyoseido_15gijigaiyo.pdf"
        source_filename: "senkyoseido_15gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_15gijigaiyo.pdf/$File/senkyoseido_15gijigaiyo.pdf"
        source_date: "2015-12-07"
        verbatim_quote: |
           定数削減について、衆議院の定数のみを減らすだけでよいと
          考えているのかとの問いに対し、参議院も含めて議員定数を
          減らすべきであると考えており、究極には一院制を導入して
          よいのではないかと考えているとの回答があった。
        position: "参議院・一院制の議論"
        speaker: "松野頼久議員（維新の党）"
        context: "衆議院定数削減に留まらず、参議院も含めた議論の必要性。"
```

---

## File: senkyoseido_16gijigaiyo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "議員定数削減の規模に関する提案"
    category: "主要論点"
    summary: "定数削減の具体的な削減幅について、4減案（総定数471）と10減案（総定数465）の二つの案が提示され、議論された。"
    spectrum:
      axis: "4減案（定数471維持） ←→ 10減案（定数465、戦後最少）"
      positions:
        - label: "4減案支持（定数維持・較差是正優先）"
          description: "将来の人口二極化を考慮すると、定数を抑制すると人口の多い地域への議席配分が困難になり、一票の較差是正に逆行するため、定数を維持すべきとの立場。"
        - label: "10減案支持（定数削減優先）"
          description: "与野党の公約を踏まえ、調査会として姿勢を示すべきであり、歴史的経緯からも最も少ない定数465人を提案すべきとの立場。"
      consensus_status: "決着(採用:10減案)"
      consensus_detail: "最終的に、本調査会においては、現行定数から10減して465人とする案がとりまとめられた。"
    evidence_chunks:
      - id: "chunk_001_1"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
          起草委員会から、定数削減について、４減案（総定数471とし、小選挙区
          を１減（０増５減を含めると５減） 、比例代表を３減する。戦後我が国が長
          い間維持してきたと考えられる本則定数である471に戻すもの。 ） と10減案
          （総定数465とし、小選挙区を５減、比例代表を５減する。衆議院議員の定
          数を戦後最少の数とするもの。 ）の提案があった。
        position: "4減案支持（定数維持・較差是正優先）"
        speaker: "委員（発言要旨）"
        context: "定数削減案の提示"
      - id: "chunk_001_2"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           将来、人口の多い地域と少ない地域とにますます二極化していく中、
          定数を抑制して人口の少ない地域に代表を確保しようとすれば、人口
          の多い地域に議席が十分に配分できなくなり、一票の較差是正に逆行
          することとなる。問題は、定数抑制と較差是正を優先するのか、定数
          を維持して較差是正を優先するのかという二者択一があり、どこでバ
          ランスをとるかということであり、定数削減の問題については、国民
          の判断に委ねるべきではないか。
        position: "4減案支持（定数維持・較差是正優先）"
        speaker: "委員（発言要旨）"
        context: "定数削減が較差是正に与える影響についての懸念"
      - id: "chunk_001_3"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           与野党とも大幅な定数削減を国民に約束しながら決められないので、
          本調査会が審議してきたわけであるから、調査会の姿勢を示すことが
          相当であり、10減案が相当と考える。
        position: "10減案支持（定数削減優先）"
        speaker: "委員（発言要旨）"
        context: "調査会の役割と公約履行の観点からの主張"
      - id: "chunk_001_4"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           歴史的経緯から見て、最も少ない定数である465人を提案することが
          よいのではないか。
        position: "10減案支持（定数削減優先）"
        speaker: "委員（発言要旨）"
        context: "歴史的観点からの定数465人支持"
      - id: "chunk_001_5"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
          本調査会においては、 衆議院議員の定数を現行定数から10減して465とし、
          小選挙区を６減、比例代表を４減する案をとりまとめた。
        position: "決着(採用:10減案)"
        speaker: "議事概要"
        context: "最終的な決定事項"

  - id: "topic_002"
    title: "定数削減と小選挙区・比例代表の配分比率"
    category: "主要論点"
    summary: "定数削減を行うにあたり、小選挙区と比例代表のどちらをどれだけ削減するかについて、現行の比率（約3:2）を維持すべきか、あるいは民意集約機能の是正のために小選挙区を重点的に削減すべきかという議論があった。"
    spectrum:
      axis: "比例代表削減優先 ←→ 小選挙区削減優先"
      positions:
        - label: "比例代表削減優先"
          description: "拘束名簿式比例代表制は有権者の選好が最も反映されにくいため、小選挙区削減よりも比例代表削減の方が国民の納得を得やすいという立場。"
        - label: "小選挙区削減優先"
          description: "民意の集約機能が行き過ぎているため、小選挙区を削減すべきであり、現行の3:2の割合が穏当であるという立場。"
      consensus_status: "両論併記（最終案は6減/4減）"
      consensus_detail: "最終案では小選挙区6減、比例代表4減（比率6:4）となったが、議論の過程では3:2維持や、小選挙区を増やして較差是正と定数削減を両立させる案なども出た。"
    evidence_chunks:
      - id: "chunk_002_1"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           比例代表を削減し、むしろ小選挙区を増やした方が較差是正と定数削
          減の両方が解決できるのではないか。
        position: "比例代表削減優先"
        speaker: "委員（発言要旨）"
        context: "小選挙区増の提案"
      - id: "chunk_002_2"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           我が国の拘束名簿式での比例代表制の下では、有権者から見ると、選
          挙の方法としては最も自分の選好が反映できないものであるので、小
          選挙区の数を減らすよりも比例代表から減らす方が国民から見ても納
          得できるのではないか。
        position: "比例代表削減優先"
        speaker: "委員（発言要旨）"
        context: "比例代表制への不満に基づく削減提案"
      - id: "chunk_002_3"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           （現在の）選挙制度にどのようなデメリット、メリットがあるかとい
          う観点からすると、民意の集約機能が行き過ぎていることはまちがい
          ないので、 小選挙区を削減すべきであると考える。（小選挙区と比例代
          表の削減の）割合については、現行の割合の３：２が穏当なところだ
          と考える。
        position: "小選挙区削減優先"
        speaker: "委員（発言要旨）"
        context: "民意集約機能是正の観点からの小選挙区削減提案"
      - id: "chunk_002_4"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           民意の集約機能が若干強過ぎると感じるので、制度のスタート時点で
          あった３：２をベースに小選挙区６減、 比例代表４減で10減すれば理
          解が得られるのではないか。
        position: "小選挙区削減優先"
        speaker: "委員（発言要旨）"
        context: "10減案の具体的な配分案（6減/4減）の根拠として3:2ベースを提示"
      - id: "chunk_002_5"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           小選挙区は既に５減しているからもうよいというのではなく、小選挙区からも削減する必要がある。
        position: "小選挙区削減優先"
        speaker: "委員（発言要旨）"
        context: "小選挙区削減の必要性の強調"

  - id: "topic_003"
    title: "将来の人口変動を見据えた定数削減の持続可能性"
    category: "課題・懸念"
    summary: "定数を削減した場合、将来的に人口較差がさらに拡大した際に、総定数を増やせない状況下で、配分を維持できるかという懸念が示された。特に、将来の人口推計を加味したアダムズ方式の導入が安定的な議席確保に寄与する可能性が指摘された。"
    spectrum:
      axis: "将来の較差拡大への懸念（定数抑制の限界） ←→ 方式変更による対応可能"
      positions:
        - label: "懸念派"
          description: "定数削減により、将来の人口較差拡大時に配分できなくなるリスクを懸念。"
        - label: "方式変更可能派"
          description: "アダムズ方式を採用すれば、将来推計人口を加味しても人口の少ない県で議席が安定的に確保されると主張。"
      consensus_status: "継続検討"
      consensus_detail: "定数削減の是非と将来の人口変動への対応策（選挙区画定方法など）は密接に関連する論点として認識された。"
    evidence_chunks:
      - id: "chunk_003_1"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           定数を削減した場合、将来、人口較差がさらに拡大したときに、本当に配分していけるかという問題を考えなければいけない。 そのときに、総定数を増やすことができないから、また比例代表から減らすというようなその場限りの対応にならないように、我が国の選挙制度が直面している問題を明確にすることが重要ではないか。
        position: "懸念派"
        speaker: "委員（発言要旨）"
        context: "定数削減後の将来的な配分可能性への懸念"
      - id: "chunk_003_2"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           将来、人口減で較差が開くとは必ずしも言えず、アダムズ方式を取り入れると、将来の推計人口を加味しても、人口の少ない県で議席数は減らず、ある程度、安定的に議席が確保されると考える。
        position: "方式変更可能派"
        speaker: "委員（発言要旨）"
        context: "アダムズ方式導入による将来の安定性確保の主張"

  - id: "topic_004"
    title: "較差是正の頻度と仕組みの強化"
    category: "主要論点"
    summary: "議員定数削減とは直接関係しないが、較差是正の議論の中で、原則10年ごとの国勢調査だけでなく、5年ごとの簡易国勢調査で較差2倍を超える選挙区が生じた場合に区画審に是正を行わせる仕組みを設けるべきとの提案があった。"
    spectrum:
      axis: "現状維持（10年ごと） ←→ 5年ごとの早期是正メカニズム導入"
      positions:
        - label: "早期是正導入支持"
          description: "5年ごとの簡易国勢調査結果に基づき、較差2倍超えで区画審による是正を義務付けるべき。"
        - label: "現状維持（議論なし）"
          description: "（特になし、早期是正導入が新たな論点として提示された）"
      consensus_status: "継続検討"
      consensus_detail: "定数削減と並行して、較差是正の頻度と即時性を高めるための具体的な仕組みの導入が論点として提起された。"
    evidence_chunks:
      - id: "chunk_004_1"
        source_doc_id: "senkyoseido_16gijigaiyo.pdf"
        source_filename: "senkyoseido_16gijigaiyo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_16gijigaiyo.pdf/$File/senkyoseido_16gijigaiyo.pdf"
        source_date: "2015-12-16"
        verbatim_quote: |
           較差是正については、 原則的に10年ごとの国勢調査で行うこととなっ
          ているが、５年ごとの簡易国勢調査の結果、較差２倍を超える選挙区
          が生じた場合には、区画審に何らかの是正を行わせる仕組みを設ける
          ことを考えるべきである。
        position: "早期是正導入支持"
        speaker: "委員（発言要旨）"
        context: "較差是正の仕組みに関する提案"
```

---

## File: senkyoseido_17gijigaiyo.pdf

提供されたドキュメント（`senkyoseido_17gijigaiyo.pdf`）は、「第17回 衆議院選挙制度に関する調査会」の議事概要であり、その議事要旨は「答申を決定し、衆議院議長に提出することとした」という事務的な結論のみが記載されています。

このドキュメントには、**「議員定数削減」**に関する具体的な論点、課題、懸念点、あるいは設計に関する議論の記述が一切含まれていません。

したがって、指定されたフィルタ（「議員定数削減」に直接関係のない内容はすべて除外）に基づき、抽出できる論点は存在しません。

```yaml
topics: []
```

---

## File: senkyoseido_chousakai.pdf

提供されたドキュメント（`senkyoseido_chousakai.pdf`）は、「衆議院選挙制度に関する調査会」の設置に関する概要文書であり、調査会の**諮問事項**を列挙しています。

このドキュメント自体は、具体的な「議員定数削減」に関する議論の中身や対立軸を示しているわけではありませんが、「議員定数削減」が調査会の**主要な検討事項の一つ**として明確に位置づけられていることが確認できます。

したがって、抽出される論点は、**「議員定数削減」を検討対象として設定したこと**、およびその**検討の進め方**に関するものとなります。

```yaml
topics:
  - id: "topic_001"
    title: "衆議院選挙制度調査会における議員定数削減の検討事項としての位置づけ"
    category: "主要論点"
    summary: "衆議院選挙制度に関する調査会が、現行制度の評価や一票の較差是正と並行して、「各党の総選挙公約にある衆議院議員定数削減の処理」を具体的な諮問事項の一つとして設定したこと。これは、定数削減が制度改革の重要な要素として扱われることを示している。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_chousakai.pdf"
        source_filename: "senkyoseido_chousakai.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_chousakai.pdf/$File/senkyoseido_chousakai.pdf"
        source_date: "平成２６年６月１９日"
        verbatim_quote: |
          三、諮問事項
            １ 現行制度を含めた選挙制度の評価（長短所、理想論と実現性）
            ２ 各党の総選挙公約にある衆議院議員定数削減の処理
            ３ 一票の較差を是正する方途
            ４ 現行憲法の下での衆参議院選挙制度の在り方の問題点
        position: null
        speaker: null
        context: "調査会への諮問事項の列挙"

  - id: "topic_002"
    title: "議員定数削減に関する答申の時期設定の考慮事項"
    category: "課題・懸念"
    summary: "議員定数削減の検討結果（答申）の時期について、現議員の任期、立法作業、および国民への周知期間を考慮して設定する必要がある点。これは、定数削減が実現する場合、そのプロセスに時間的制約と政治的・制度的準備期間が必要であることを示唆している。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_002"
        source_doc_id: "senkyoseido_chousakai.pdf"
        source_filename: "senkyoseido_chousakai.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_chousakai.pdf/$File/senkyoseido_chousakai.pdf"
        source_date: "平成２６年６月１９日"
        verbatim_quote: |
          五、答 申
            ３ 答申の時期については、現議員の任期を念頭に、立法作業や周知期間を考
            え答申願う（従って、答申が累次のものとなることも予想される） 。
        position: null
        speaker: null
        context: "答申の時期に関する指示"
```

---

## File: senkyoseido_chousakai_1.pdf

ドキュメント（senkyoseido_chousakai_1.pdf）を読み込み、「議員定数削減」に直接関連する論点を抽出します。

このドキュメントは「衆議院選挙制度に関する調査会」の設置要綱であり、諮問事項として「各党の総選挙公約にある衆議院議員定数削減の処理」が明記されています。これは、定数削減が調査会の主要な検討事項の一つであることを示しています。

```yaml
topics:
  - id: "topic_001"
    title: "衆議院議員定数削減の処理"
    category: "主要論点"
    summary: "各政党の公約に含まれている衆議院議員定数削減について、調査会が具体的な処理方法を検討・集約することが諮問事項とされている。これは、定数削減の是非や具体的な方法論が調査会の中心的な課題の一つであることを示している。"
    spectrum:
      axis: "定数削減の実施 ←→ 慎重な検討"
      positions:
        - label: "公約実現派"
          description: "各党の公約に基づき、定数削減を具体的に進めるべきとする立場。"
        - label: "慎重派"
          description: "定数削減の実現性や、選挙制度全体への影響を考慮し、慎重に進めるべきとする立場。"
      consensus_status: "継続検討"
      consensus_detail: "調査会がこの論点について具体的な処理方法を検討し、答申することが求められているため、現時点では結論が出ていない。"
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_chousakai_1.pdf"
        source_filename: "senkyoseido_chousakai_1.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_annai.nsf/html/statics/shiryo/senkyoseido_index.html"
        source_date: "平成２６年６月１９日"
        verbatim_quote: |
          三、諮問事項
            ２ 各党の総選挙公約にある衆議院議員定数削減の処理
        position: null
        speaker: null
        context: "調査会の諮問事項として明記されている点。"

  - id: "topic_002"
    title: "調査会の答申時期と立法・周知期間の考慮"
    category: "課題・懸念"
    summary: "定数削減を含む調査会の答申は、現議員の任期を念頭に置き、その後の立法作業や国民への周知期間を考慮して行われる必要がある。これにより、答申が一度で終わらず、累次的なものになる可能性が示唆されており、スケジュール管理が課題となる。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_002"
        source_doc_id: "senkyoseido_chousakai_1.pdf"
        source_filename: "senkyoseido_chousakai_1.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_annai.nsf/html/statics/shiryo/senkyoseido_index.html"
        source_date: "平成２６年６月１９日"
        verbatim_quote: |
          五、答 申
            ３ 答申の時期については、現議員の任期を念頭に、立法作業や周知期間を考
          え答申願う（従って、答申が累次のものとなることも予想される） 。
        position: null
        speaker: null
        context: "答申の時期に関する規定。定数削減の実現には、このスケジュール感が重要となる。"
```

---

## File: senkyoseido_iinmeibo.pdf

提供されたドキュメント `senkyoseido_iinmeibo.pdf` は、「衆議院選挙制度に関する調査会 委員名簿」であり、調査会の構成員（委員の氏名、肩書き）が記載されているのみです。

このドキュメントには、**「議員定数削減」**に関する具体的な議論、論点、課題、懸念点、あるいは新たなアイデアは一切含まれていません。

したがって、指定されたフィルタ（「議員定数削減」に直接関係のない内容はすべて除外）に基づき、抽出できる論点は存在しません。

```yaml
topics: []
```

---

## File: senkyoseido_iinmeibo_1.pdf

提供されたドキュメント（`senkyoseido_iinmeibo_1.pdf`）は、「衆議院選挙制度に関する調査会 委員名簿」であり、調査会の構成員（委員の氏名、肩書き）が記載されているのみです。

このドキュメントには、**「議員定数削減」**に関する具体的な議論、論点、課題、懸念点、あるいは新たなアイデアは一切含まれていません。

したがって、**「議員定数削減」に関連する論点を抽出することはできません**。

以下に、指示されたYAML形式で、抽出された論点がないことを示す形で出力します。

```yaml
topics: []
```

---

## File: senkyoseido_kyougikai.pdf

このドキュメントは「衆議院選挙制度に関する協議会」の設置要綱であり、その目的として「議員定数や地域の実情を反映した選挙区割りの在り方等に関し、国会において抜本的な検討を行う」ことが明記されています。

しかし、この文書自体は**協議会の設置と運営に関する規定**であり、**具体的な「議員定数削減」の是非や削減案そのものに関する議論や論点**は含まれていません。

唯一、議員定数に関わる検討の背景として言及されているのは、人口減少と地域間格差を是正するための「抜本的な検討」の必要性です。これは「議員定数削減」の議論の**前提**ではありますが、削減の具体的な論点や課題を提示するものではありません。

したがって、**「議員定数削減」に直接関係する具体的な論点、課題、懸念点、アイデアを抽出することは、この資料からはできません**。

以下に、この文書から抽出できる、選挙制度検討の**前提**に関する情報を、指定されたフォーマットで出力します。

```yaml
topics:
  - id: "topic_001"
    title: "衆議院選挙制度の抜本的検討の必要性（人口減少・地域間格差への対応）"
    category: "主要論点"
    summary: "協議会設置の目的として、人口減少と地域間格差が拡大している現状を踏まえ、議員定数や選挙区割りの在り方について抜本的な検討を行うことが掲げられている。これは、議員定数削減を含む制度改革の必要性の根拠となる。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "senkyoseido_kyougikai.pdf"
        source_filename: "senkyoseido_kyougikai.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_kyougikai.pdf/$File/senkyoseido_kyougikai.pdf"
        source_date: "2024-12-19"
        verbatim_quote: |
          衆議院の選挙制度について、 人口減少や地域間格差が拡大している現状を踏まえ
          つつ、立法府の在り方を含め、議員定数や地域の実情を反映した選挙区割りの在り
          方等に関し、国会において抜本的な検討を行うため、衆議院議長（以下「議長」と
          いう。 ）の下に衆議院選挙制度に関する協議会（以下「協議会」という。 ）を置く。
        position: null
        speaker: null
        context: "協議会設置の目的"
  - id: "topic_002"
    title: "検討の対象事項（定数・区割りに影響する過去の決定事項）"
    category: "主要論点"
    summary: "協議会が検討すべき事項として、過去の倫理選挙特別委員会の附帯決議や、与野党会談で整理された事項が指定されており、これらが議員定数や選挙区割りの具体的な検討の出発点となる。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_002"
        source_doc_id: "senkyoseido_kyougikai.pdf"
        source_filename: "senkyoseido_kyougikai.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_kyougikai.pdf/$File/senkyoseido_kyougikai.pdf"
        source_date: "2024-12-19"
        verbatim_quote: |
          （１） 協議会の検討の対象は、衆議院の選挙制度に関する次の事項とする。
            ➀ 衆議院倫理選挙特別委員会の附帯決議（令和４年11月８日）の検討事項
            ② 与野党６党の国対委員長会談の要請を受けて設置された 「衆議院選挙制度協
          議会」の報告書（令和５年12月）において整理された事項
        position: null
        speaker: null
        context: "協議会の検討対象事項の定義"
  - id: "topic_003"
    title: "結論を得るための期限設定（国勢調査結果の活用）"
    category: "課題・懸念"
    summary: "協議会は、過去の附帯決議を踏まえ、令和7年の国勢調査の結果が判明する時点を目途に具体的な結論を得るよう努力することが求められており、これは定数・区割り決定のスケジュールに制約を与える。"
    spectrum: null
    evidence_chunks:
      - id: "chunk_003"
        source_doc_id: "senkyoseido_kyougikai.pdf"
        source_filename: "senkyoseido_kyougikai.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_kyougikai.pdf/$File/senkyoseido_kyougikai.pdf"
        source_date: "2024-12-19"
        verbatim_quote: |
          （４） 協議会は、（１）①の附帯決議を踏まえ、令和７年の国勢調査の結果が判明
          する時点を目途に具体的な結論を得るよう努力するものとする。
        position: null
        speaker: null
        context: "協議会の目標設定"
```

---

## File: senkyoseido_kyougikai_iinmeibo.pdf

提供されたドキュメント `senkyoseido_kyougikai_iinmeibo.pdf` は、「衆議院選挙制度に関する協議会」の協議員名簿であり、**令和7年11月17日時点の構成員リスト**を示しています。

このドキュメント自体には、「議員定数削減」に関する具体的な議論、論点、課題、懸念点、あるいは新たなアイデアは**一切含まれていません**。含まれているのは、協議会の構成員（座長および協議員）の氏名と所属政党のみです。

したがって、**「議員定数削減」に直接関連する論点を抽出することはできません**。

以下に、指示されたフォーマットに従い、抽出された論点がないことを示すYAML構造を出力します。

```yaml
topics: []
```

---

## File: senkyoseido_toshin.pdf

```yaml
topics:
  - id: "topic_001"
    title: "定数削減の是非に関する基本的な考え方"
    category: "主要論点"
    summary: "定数削減の必要性について、国際比較や過去の経緯からは削減の積極的な理由や理論的根拠は見出し難いとする一方で、国民との約束として削減案を検討する必要性が示されている。"
    spectrum:
      axis: "削減不要論 ←→ 国民との約束論"
      positions:
        - label: "削減不要論"
          description: "国際比較や過去の経緯から、現行定数は多いとは言えず、削減する積極的な理由や理論的根拠は見出し難い。"
        - label: "国民との約束論"
          description: "衆議院議員の定数削減は多くの政党の選挙公約であり、主権者たる国民との約束であるため、削減案を求められる。"
      consensus_status: "両論併記"
      consensus_detail: "定数削減の是非について、学術的・客観的な根拠と、政治的要請（公約）の双方を考慮し、具体的な削減案を提示する形で対応している。"
    evidence_chunks:
      - id: "chunk_001_1"
        source_doc_id: "senkyoseido_toshin.pdf"
        source_filename: "senkyoseido_toshin.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshin.pdf/$File/senkyoseido_toshin.pdf"
        source_date: "平成28年1月"
        verbatim_quote: |
          （１）現行の衆議院議員の定数は、国際比較や過去の経緯などからすると多いとは
          言えず、これを削減する積極的な理由や理論的根拠は見出し難い。
        position: "削減不要論"
        speaker: null
        context: "定数削減に関する調査会の結論（２．定数削減の冒頭）"
      - id: "chunk_001_2"
        source_doc_id: "senkyoseido_toshin.pdf"
        source_filename: "senkyoseido_toshin.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshin.pdf/$File/senkyoseido_toshin.pdf"
        source_date: "平成28年1月"
        verbatim_quote: |
          （２）一方、衆議院議員の定数削減は多くの政党の選挙公約であり、主権者たる国
          民との約束である。
        position: "国民との約束論"
        speaker: null
        context: "定数削減に関する調査会の結論（２．定数削減）"

  - id: "topic_002"
    title: "具体的な定数削減案の提示"
    category: "主要論点"
    summary: "定数削減を求められる場合に備え、総定数10人削減（465人）案と、それに伴う小選挙区・比例代表の定数内訳削減案が具体的に提示されている。"
    spectrum:
      axis: "総定数削減案の提示"
      positions:
        - label: "総定数削減案"
          description: "総定数を10人削減し465人とする。"
        - label: "内訳削減案"
          description: "小選挙区を6人削減（289人）、比例代表を4人削減（176人）とする。"
      consensus_status: "採用:総定数削減案"
      consensus_detail: "削減案を求められる場合の具体的な選択肢として提示された。"
    evidence_chunks:
      - id: "chunk_002_1"
        source_doc_id: "senkyoseido_toshin.pdf"
        source_filename: "senkyoseido_toshin.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshin.pdf/$File/senkyoseido_toshin.pdf"
        source_date: "平成28年1月"
        verbatim_quote: |
          このことから、削減案を求められるとするならば、以下の案が考えられる。
          ① 衆議院議員の定数を10人削減して465人とする。
          ② 小選挙区選挙と比例代表選挙のそれぞれの定数は、 小選挙区選挙の定数を
          ６人削減して289人とし、 比例代表選挙の定数を４人削減して176人とする。
        position: "総定数削減案"
        speaker: null
        context: "定数削減案の提示"

  - id: "topic_003"
    title: "定数削減と一票の較差是正の関連性"
    category: "課題・懸念"
    summary: "定数削減の是非とは別に、制度の信頼性確保のため、人口動態に合わせた選挙区の見直しと較差是正が喫緊の最重要課題であると位置づけられている。定数削減が実施される場合、この較差是正の仕組みが同時に重要となる。"
    spectrum:
      axis: "較差是正の優先度"
      positions:
        - label: "較差是正の最重要課題化"
          description: "制度の信頼性確保のため、較差是正は喫緊の最重要課題である。"
        - label: "定数削減の前提"
          description: "定数削減の議論とは別に、較差是正の仕組みを構築する必要がある。"
      consensus_status: "継続検討"
      consensus_detail: "定数維持の立場であっても、較差是正は最重要課題とされているため、定数削減の有無にかかわらず、較差是正の具体的な手法（アダムズ方式、10年ごとの見直し等）の検討が不可欠である。"
    evidence_chunks:
      - id: "chunk_003_1"
        source_doc_id: "senkyoseido_toshin.pdf"
        source_filename: "senkyoseido_toshin.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshin.pdf/$File/senkyoseido_toshin.pdf"
        source_date: "平成28年1月"
        verbatim_quote: |
          現行の小選挙区比例代表並立制を維持する。
          ただし、制度の信頼性を確保するため、人口動態に合わせて、選挙区間の一票の
          較差、選挙区の区割りなどを定期的に見直す仕組みとする必要がある。その点から
          して、較差是正は喫緊の最重要課題である。
        position: null
        speaker: null
        context: "衆議院議員の選挙制度の在り方に関する結論（１．）"
```

---

## File: senkyoseido_toshinsankoshiryo.pdf

```yaml
topics:
  - id: "topic_001"
    title: "衆議院議員定数削減の必要性と処理"
    category: "主要論点"
    summary: "調査会設置の諮問事項の一つとして、各党の総選挙公約にある衆議院議員定数削減の処理が挙げられており、これは選挙制度改革における中心的な論点の一つである。"
    spectrum:
      axis: "定数削減の実施時期と規模"
      positions:
        - label: "公約に基づき削減を推進すべき立場"
          description: "各党の公約にある定数削減を具体的に処理する必要があるとする立場。"
        - label: "一票の較差是正を優先すべき立場"
          description: "定数削減よりも、一票の較差是正が喫緊の課題であるとする立場。"
      consensus_status: "継続検討"
      consensus_detail: "諮問事項として挙げられているが、本資料からは具体的な削減規模や時期に関する合意形成の状況は不明。"
    evidence_chunks:
      - id: "chunk_001_01"
        source_doc_id: "senkyoseido_toshinsankoshiryo.pdf"
        source_filename: "senkyoseido_toshinsankoshiryo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshinsankoshiryo.pdf/$File/senkyoseido_toshinsankoshiryo.pdf"
        source_date: "2014-06-19"
        verbatim_quote: |
          三、諮問事項
          ...
          ２ 各党の総選挙公約にある衆議院議員定数削減の処理
        position: null
        speaker: null
        context: "調査会の諮問事項"

  - id: "topic_002"
    title: "一票の較差是正の必要性"
    category: "主要論点"
    summary: "一票の較差是正は、調査会の主要な諮問事項であり、選挙制度改革の根幹に関わる論点である。特に、過去の最高裁判決や高裁判決がこの問題に言及していることが示唆されている。"
    spectrum:
      axis: "較差是正の緊急度"
      positions:
        - label: "較差是正を最優先すべき立場"
          description: "一票の較差是正が、定数削減よりも優先されるべき課題であるとする立場。"
        - label: "定数削減と並行して検討すべき立場"
          description: "定数削減と較差是正を同時に、あるいは関連付けて検討すべきとする立場。"
      consensus_status: "継続検討"
      consensus_detail: "最高裁・高裁判決のまとめが議論に含まれており、法的な要請として較差是正の重要性が認識されている。"
    evidence_chunks:
      - id: "chunk_002_01"
        source_doc_id: "senkyoseido_toshinsankoshiryo.pdf"
        source_filename: "senkyoseido_toshinsankoshiryo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshinsankoshiryo.pdf/$File/senkyoseido_toshinsankoshiryo.pdf"
        source_date: "2014-06-19"
        verbatim_quote: |
          三、諮問事項
          ...
          ３ 一票の較差を是正する方途
        position: null
        speaker: null
        context: "調査会の諮問事項"
      - id: "chunk_002_02"
        source_doc_id: "senkyoseido_toshinsankoshiryo.pdf"
        source_filename: "senkyoseido_toshinsankoshiryo.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshinsankoshiryo.pdf/$File/senkyoseido_toshinsankoshiryo.pdf"
        source_date: "2016-01-14"
        verbatim_quote: |
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申案討議」 
          １２．１６（月） 第１６回 「答申

---

## File: senkyoseido_toshinsetsumei.pdf

```yaml
topics:
  - id: "topic_001"
    title: "衆議院議員定数削減の是非と削減案"
    category: "主要論点"
    summary: "定数削減の積極的な理由や理論的根拠は見出し難いが、多くの政党の選挙公約であるため、国民との約束として尊重し、もし削減するならば10人削減（465人）が考えられるという結論。"
    spectrum:
      axis: "削減しない（現状維持） ←→ 削減する（公約尊重）"
      positions:
        - label: "削減に積極的理由なし"
          description: "国際比較や過去の経緯から見て、現行定数は多いとは言えず、削減する積極的な理由や理論的根拠は見出し難い。"
        - label: "公約として削減を尊重"
          description: "定数削減は多くの政党の選挙公約であり、主権者たる国民との約束であるため、削減案を求められるならば10人削減（465人）が考えられる。"
      consensus_status: "決着(採用:10人削減案)"
      consensus_detail: "積極的な理由はないものの、公約尊重の観点から、大正14年以降で最も少ない465人への10人削減案が結論とされた。"
    evidence_chunks:
      - id: "chunk_001_1"
        source_doc_id: "senkyoseido_toshinsetsumei.pdf"
        source_filename: "senkyoseido_toshinsetsumei.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshinsetsumei.pdf/$File/senkyoseido_toshinsetsumei.pdf"
        verbatim_quote: |
          （１）現行の衆議院議員の定数 は、国際比較や過去の経緯などからすると多いとは言
          えず、これを削減する積極的な理由 や理論的根拠 は見出し難い。
        position: "削減に積極的理由なし"
        speaker: null
        context: "定数削減に関する結論に至る経緯・理由の冒頭"
      - id: "chunk_001_2"
        source_doc_id: "senkyoseido_toshinsetsumei.pdf"
        source_filename: "senkyoseido_toshinsetsumei.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshinsetsumei.pdf/$File/senkyoseido_toshinsetsumei.pdf"
        verbatim_quote: |
          しかしながら、 定数の削減は、 ヒアリングを実施した 政党のうち日本共産
          党及び社会民主党を除く すべての政党の選挙公約であり、 多くの政党の選
          挙公約は、いわば公党の 国民との約束 として、できる限り 尊重されなけれ
          ばならない。
        position: "公約として削減を尊重"
        speaker: null
        context: "定数削減に関する結論に至る経緯・理由"
      - id: "chunk_001_3"
        source_doc_id: "senkyoseido_toshinsetsumei.pdf"
        source_filename: "senkyoseido_toshinsetsumei.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshinsetsumei.pdf/$File/senkyoseido_toshinsetsumei.pdf"
        verbatim_quote: |
          以上の諸点を総合的に勘案し、 もし削減案を求められるとするならば、 衆議院議員 の定数は、 10 人削減して 465 人とする案が考えられる 。これは、大正 14 年に男子による普通選挙が実現して以降、 最も少ない数 となる。
        position: "決着(採用:10人削減案)"
        speaker: null
        context: "定数削減に関する結論に至る経緯・理由"

  - id: "topic_002"
    title: "定数削減時の小選挙区・比例代表の配分比率維持"
    category: "主要論点"
    summary: "定数を削減する場合、小選挙区と比例代表の定数配分については、現行制度発足時の割合（300:200）に基づき、それぞれ6人削減（289人）と4人削減（176人）とすることが適当とされた。"
    spectrum:
      axis: "現行比率維持 ←→ 他の比率案"
      positions:
        - label: "現行比率維持"
          description: "小選挙区選挙と比例代表選挙の定数について、現行制度発足時の両者の定数の割合（300人対200人）により削減する。"
        - label: "その他"
          description: "他の削減案の検討は行われていない。"
      consensus_status: "決着(採用:現行比率維持)"
      consensus_detail: "定数削減（10人減）に伴い、小選挙区を6人減（289人）、比例代表を4人減（176人）とする案が採用された。"
    evidence_chunks:
      - id: "chunk_002_1"
        source_doc_id: "senkyoseido_toshinsetsumei.pdf"
        source_filename: "senkyoseido_toshinsetsumei.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshinsetsumei.pdf/$File/senkyoseido_toshinsetsumei.pdf"
        verbatim_quote: |
          その場合、 小選挙区 選挙と比例代表 選挙の定数について は、現行制度発足
          時の両者の定数の割合（300 人対 200 人）により削減することとし 、小選
          挙区選挙の定数を６人削減して 289 人、比例代表 選挙の定数を４人削減し
          て 176 人とすることが適当である 。
        position: "現行比率維持"
        speaker: null
        context: "定数削減に関する結論に至る経緯・理由"

  - id: "topic_003"
    title: "定数削減が較差是正に与える影響（課題）"
    category: "課題・懸念"
    summary: "定数を大幅に削減すると、都道府県間の一票の較差、ひいては選挙区間の一票の較差の縮小が難しくなるという懸念がある。定数削減と較差最小化の要請を同時に達成することは困難である。"
    spectrum:
      axis: "定数削減優先 ←→ 較差是正優先"
      positions:
        - label: "較差是正の困難化"
          description: "大幅な定数削減は、較差是正を困難にする。"
        - label: "定数削減の必要性"
          description: "公約尊重のため削減は必要である。"
      consensus_status: "両論併記"
      consensus_detail: "定数削減は公約として受け入れられたが、その結果として較差是正の難易度が上がるというトレードオフが存在する。"
    evidence_chunks:
      - id: "chunk_003_1"
        source_doc_id: "senkyoseido_toshinsetsumei.pdf"
        source_filename: "senkyoseido_toshinsetsumei.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshinsetsumei.pdf/$File/senkyoseido_toshinsetsumei.pdf"
        verbatim_quote: |
          小選挙区 選挙において、 都道府県を単位 に議席配分する ことを前提として
          大幅に定数を削減すると 、都道府県間の一票の較差 、ひいては選挙区間の
          一票の較差の縮小は難しくな る。定数の大幅削減と 議席の比例配分及び 較
          差の最小化 という要請を 同時に達成すること は困難である。
        position: "較差是正の困難化"
        speaker: null
        context: "定数削減に関する結論に至る経緯・理由"

  - id: "topic_004"
    title: "定数削減が国会機能に与える影響（懸念）"
    category: "課題・懸念"
    summary: "定数削減は、有為な人材を集めることによる国民の代表としての機能強化や、行政府との緊張関係維持、各種委員会の機能充実といった観点から、マイナスに作用する可能性がある。"
    spectrum:
      axis: "機能強化（削減反対） ←→ 定数削減（公約尊重）"
      positions:
        - label: "機能低下の懸念"
          description: "議員数を考える際、有為な人材の確保や国会機能の強化の観点も考慮する必要がある。"
        - label: "公約尊重"
          description: "公約尊重のため削減は必要である。"
      consensus_status: "両論併記"
      consensus_detail: "機能強化の観点からは削減は望ましくないものの、公約尊重のため削減が容認された。"
    evidence_chunks:
      - id: "chunk_004_1"
        source_doc_id: "senkyoseido_toshinsetsumei.pdf"
        source_filename: "senkyoseido_toshinsetsumei.pdf"
        source_url: "https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_toshinsetsumei.pdf/$File/senkyoseido_toshinsetsumei.pdf"
        verbatim_quote: |
          議員数を考えるに際しては、 議席は有権者に とっては選ぶ権利であるとい
          う視点、また、 有為な人材を集め ることによる 国民の代表 議会としての 国
          会の機能強化、行政府 との緊張関係の維持 、各種委員会の機能 の充実など
          の諸要素 を考慮する必要がある。
        position: "機能低下の懸念"
        speaker: null
        context: "定数削減に関する結論に至る経緯・理由"
```

---

