# 最終成果物 (Q&Aリスト)

```yaml
topics:
  - id: "topic_001"
    title: "電子船荷証券の法的性質と譲渡方法の確立（類型設定と効力構成）"
    category: "主要論点"
    summary: "電子船荷証券（電磁的船荷証券記録）の法律上の名称は「電子船荷証券記録」と決定された。これは、船荷証券に記載すべき事項を記録した電磁的記録であり、特定情報処理システムで作成・管理され、改変確認措置や作成者証明措置がとられているものを指す。名称に「証券」を含めることによる誤解回避と国際動向との整合性が考慮された。また、既に実務で利用されている規約ベースの電子B/L（かぎかっこ付き電子B/L）を、新たな法制度でどのように位置づけ、既存の実務を阻害しないように定義するかが大きな論点となっている。法的性質については、①船荷証券そのものの電子化（物・有価証券とみなす）、②支配概念の創出、③債権譲渡に着目するアプローチの3案が検討されたが、最終的には①案を前提としつつ、紙の規定との対応を個別規定で整理する方針が示された。また、紙の船荷証券の利用継続は相当との見解で一致している。譲渡方法については、紙の船荷証券の4類型（指図証券型、記名式所持人払証券型、裏書禁止型、無記名証券型）を維持するか否か（A案、B案、C案）が論点となったが、明確な方向性は出ず継続検討。A案では指図証券型を規律せず、裏書に相当する行為を不要とする案が示されたが、裏書に相当する行為の規律自体は引き続き検討が必要とされた。留置権や質権の客体とすることはできないとの整理がなされた。また、複数通発行は認めない方針が示された。"
    spectrum:
      axis: "A案（2類型） ←→ B案（4類型維持）"
      positions:
        - label: "電磁的船荷証券記録を支持する立場"
          description: "既存の用語に倣い、また磁気的方式も含む観念的な正確性から「電磁的」が適切。"
        - label: "電子船荷証券記録を支持する立場"
          description: "国際動向（MLETR, Law Commission草案）では'electronic'が用いられており、無用な誤解を避けるため「電子」を選択することも可能。"
        - label: "電子船荷証券記録案"
          description: "「船荷証券」と機能的同等性を持つ電磁的記録として、分かりやすさと国際動向を踏まえ「電子船荷証券記録」とする。"
        - label: "既存実務の尊重・包含"
          description: "現に存在する規約ベースの電子B/Lを否定せず、それらも法的に認められるよう定義を慎重に定めるべき。"
        - label: "①案（物・有価証券）"
          description: "電磁的記録を商法上の「船荷証券」並びに民法上の「物」及び「有価証券」とする考え方。担保物権の客体化が可能だが、民法上の「物」の概念拡張に慎重な検討が必要。"
        - label: "②案（支配概念）"
          description: "電磁的記録を「船荷証券」「物」「有価証券」とはせず、排他的な「支配」という新概念を創出し、「支配」の移転に裏書と同一の効力を認める方向。"
        - label: "③案（債権譲渡）"
          description: "運送品の引渡しに係る債権の移転という実体に着目し、電磁的記録の移転を債権譲渡の効力要件かつ対抗要件とする考え方。電子記録債権法や社債等の振替に関する法律の考え方と親和的。"
        - label: "①案支持（機能的同等性重視）"
          description: "電磁的船荷証券記録に紙の船荷証券と同一の効力を認める方向性。MLETR等との親和性が高い。"
        - label: "②案支持（債権譲渡構成）"
          description: "運送品の引渡しに係る債権の移転という実体面に着目し、支配の移転を債権譲渡の効力要件・対抗要件とする方向性。"
        - label: "A案（2類型）"
          description: "指図証券型を規律せず、裏書禁止型とそれ以外の2類型（実質的に指図証券型を含む）とする案。制度の単純化を目指す。"
        - label: "B案（4類型維持）"
          description: "紙の船荷証券の4類型をそのまま維持する案。理論上の観念可能性を重視。"
        - label: "C案（2類型）"
          description: "実務上ほとんど利用されない記名式所持人払証券型と無記名証券型を規律せず、指図証券型と裏書禁止型の2類型のみとする案。"
        - label: "裏書相当行為を不要とする（A案）"
          description: "A案を採用した場合、指図証券型と解される場合でも、裏書に相当する行為（支配の移転者の氏名等の記録）は不要となる。"
        - label: "転換請求権を認める（Y案）"
          description: "電磁的船荷証券記録の支配を有する者に、運送人に対する紙の船荷証券への転換請求権を認める案。"
        - label: "転換請求権を認めない（X案）"
          description: "転換請求権を認めず、原則として電磁的船荷証券記録の支配を有する者と運送人の双方の合意がある場合にのみ紙への転換を認める案。"
        - label: "甲案（効力喪失）"
          description: "強制執行手続を優先し、電磁的船荷証券記録の効力を喪失させる案。"
        - label: "乙案（有価証券とみなす）"
          description: "転換請求権を前提とし、債権者がこれを代位行使する手段を確保する案。"
        - label: "留置権の適用を断念"
          description: "電磁的船荷証券記録は民法上の「物」ではないため、留置権や質権等の担保物権の客体とすることはできない。"
        - label: "喪失手続は不要"
          description: "電磁的船荷証券記録は紛失しにくいため、紙の船荷証券のような喪失手続は不要。"
        - label: "複数通発行を認めない（1通のみ）"
          description: "電磁的船荷証券記録は紛失しにくく、複数通発行を認めると取引の安全が害されるため、1通のみとする。"
        - label: "柔軟な技術要件・認証機関不要"
          description: "技術要件を省令に委任し柔軟性を持たせ、国の認証機関による関与を必須としない。"
      consensus_status: "継続検討"
      consensus_detail: "名称は「電子船荷証券記録」とすることが決定された。法的性質については3案が提示され、①案を前提としつつ、紙の規定との対応を個別規定で整理する方針が示されたが、①案の民法上の「物」の概念拡張については慎重論がある。類型設定についてはA案、B案、C案が提示されたが明確な方向性は出ず継続検討。効力構成についても①案と②案が併記され継続検討。紙の船荷証券の利用継続は相当との見解で一致した。裏書に相当する行為の規律については引き続き検討が必要とされた。"
    evidence_chunks:
      - id: "chunk_001"
        source_doc_id: "001373713.pdf"
        source_filename: "001373713.pdf"
        source_url: "https://www.moj.go.jp/content/001373713.pdf"
        source_date: "令和4年4月27日"
        verbatim_quote: |
          また、本資料においては、電子化された船荷証券を「電磁的船荷証券記録」
          と呼称することとしているが、電子化された船荷証券の名称について、どのよう
          に考えるか。
        position: "電磁的船荷証券記録を支持する立場"
        speaker: null
        context: "初期の名称に関する検討事項"
      - id: "chunk_002"
        source_doc_id: "001377877.pdf"
        source_filename: "001377877.pdf"
        source_url: "https://www.moj.go.jp/content/001377877.pdf"
        source_date: "令和4年7月27日"
        verbatim_quote: |
          そして、「電磁的」という用語を英語に翻訳すると、一般的には、“electronic 
          or magnetic”という表記が用いられる可能性が高いところ（注１）、海外法制の動
          向を見ると、MLETRやシンガポール法では“electro transferable record”、イギ
          リスのLaw Commission草案では“electronic trade document”といった用語が用
          いられており、いずれも“magnetic”という単語は用いられていない。
        position: "電子船荷証券記録を支持する立場"
        speaker: null
        context: "国際動向との比較"
      - id: "chunk_003"
        source_doc_id: "001390064.pdf"
        source_filename: "001390064.pdf"
        source_url: "https://www.moj.go.jp/content/001390064.pdf"
        source_date: "令和5年1月25日"
        verbatim_quote: |
          今回の法改正で実現しようとする電子化された船荷証券の法律上の名称を「電子
          船荷証券記録」とする。
        position: "電子船荷証券記録案"
        speaker: "法案検討事項"
        context: "第1部 第1 電子化された船荷証券の名称"
      - id: "chunk_004"
        source_doc_id: "001390064.pdf"
        source_filename: "001390064.pdf"
        source_url: "https://www.moj.go.jp/content/001390064.pdf"
        source_date: "令和5年1月25日"
        verbatim_quote: |
          名称の末尾が「証券」で終わることになると、紙面の存在が前提となっているかのような誤解を生じさせるおそれも否定できない。
        position: "電子船荷証券記録案"
        speaker: null
        context: "名称決定の理由"
      - id: "chunk_005"
        source_doc_id: "001394827.pdf"
        source_filename: "001394827.pdf"
        source_url: "https://www.moj.go.jp/content/001394827.pdf"
        source_date: "令和5年3月8日"
        verbatim_quote: |
          今回の法改正で実現しようとする電子化された船荷証券の法律上の名称を「電
          子船荷証券記録」とする。
        position: "電子船荷証券記録案"
        speaker: "法案検討事項"
        context: "第1部 第1 電子化された船荷証券の名称"
      - id: "chunk_006"
        source_doc_id: "001422019.pdf"
        source_filename: "001422019.pdf"
        source_url: "https://www.moj.go.jp/content/001422019.pdf"
        source_date: "令和6年7月24日"
        verbatim_quote: |
          これまでの調査審議を踏まえて、電子化された船荷証券の名称を「電子船荷証券記録」としている。
        position: "電子船荷証券記録案"
        speaker: null
        context: "名称決定の補足説明"
      - id: "chunk_007"
        source_doc_id: "001408123.pdf"
        source_filename: "001408123.pdf"
        source_url: "https://www.moj.go.jp/content/001408123.pdf"
        source_date: "令和6年7月24日"
        verbatim_quote: |
          電子化された船荷証券の法律上の名称については、引き続き検討すべきものであるが、第３回会議での議論の状況に鑑み、本部会資料においては「電子船荷証券記録」との名称を仮に用いることとする。
        position: "電子船荷証券記録案"
        speaker: "法案検討事項"
        context: "前注：電子化された船荷証券の名称に関する方針"
      - id: "chunk_008"
        source_doc_id: "001394827.pdf"
        source_filename: "001394827.pdf"
        source_url: "https://www.moj.go.jp/content/001394827.pdf"
        source_date: "令和5年3月8日"
        verbatim_quote: |
          電子化された船荷証券の法律上の名称を「電子船荷証券記録」とする。
        position: "電子船荷証券記録案"
        speaker: "法案検討事項"
        context: "第1部 第1 電子化された船荷証券の名称"
      - id: "chunk_009"
        source_doc_id: "001394827.pdf"
        source_filename: "001394827.pdf"
        source_url: "https://www.moj.go.jp/content/001394827.pdf"
        source_date: "令和5年3月8日"
        verbatim_quote: |
          海外法制の動向を見ると、MLETR やシンガポール法では“electro transferable record”、イギリスのLaw Commissionの２０２２年３月１５日の「電子取引文書－報告書及び草案」...では“electronic trade document”といった用語が用いられており、いずれも“magnetic”という単語は用いられていない。
        position: "電子船荷証券記録案"
        speaker: null
        context: "名称選定の理由（国際調和）"
      - id: "chunk_010"
        source_doc_id: "001408123.pdf"
        source_filename: "001408123.pdf"
        source_url: "https://www.moj.go.jp/content/001408123.pdf"
        source_date: "令和6年7月24日"
        verbatim_quote: |
          電子化された船荷証券の法律上の名称については、引き続き検討すべきものであるが、第３回会議での議論の状況に鑑み、本部会資料においては「電子船荷証券記録」との名称を仮に用いることとする。
        position: "電子船荷証券記録案"
        speaker: "法案検討事項"
        context: "前注：電子化された船荷証券の名称に関する方針"
      - id: "chunk_011"
        source_doc_id: "20210414diji01_minutes.pdf"
        source_filename: "20210414diji01_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/790/20210414digi01_minutes.pdf"
        source_date: "2021-04-14"
        verbatim_quote: |
          正直、実務の感覚としては今回の法律で、なまじ変な電子 B/L の定義がされること
          によって、現に七つあるものを不用意な形でえり分けて効果に差を与える、あるいはいわ
          んや、もし日本発のものだけが電子 B/L と認められるとなれば、国際摩擦にもなりかねな
          い話です。その意味で電子B/L の定義をどうするかは、相当慎重に考える必要があると
          思っています。
        position: "既存実務の尊重・包含"
        speaker: "（Ｅ）委員"
        context: "規約ベースの電子B/Lの現状認識と定義の重要性について"
      - id: "chunk_012"
        source_doc_id: "20210414diji01_minutes.pdf"
        source_filename: "20210414diji01_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/790/20210414digi01_minutes.pdf"
        source_date: "2021-04-14"
        verbatim_quote: |
          民間ベースで、しかし国際的な団体における認証という形
          で、ある程度、民間の中での自律的な規律の上に働いているのだから、それ以上のことは
          する必要がないのではないかと思っているという、 それ以上でもそれ以下でもないのです。
        position: "既存実務の尊重・包含"
        speaker: "（Ｅ）委員"
        context: "民間ベースの自律的な規律を尊重すべきという意見"
      - id: "chunk_013"
        source_doc_id: "20210414diji01_minutes.pdf"
        source_filename: "20210414diji01_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/790/20210414digi01_minutes.pdf"
        source_date: "2021-04-14"
        verbatim_quote: |
          あくまで私法的な定義を、できるだけ概括的に作って、七つあるいは八つになるいろいろなプロバイダーのサービスがイコールフッティングで競争できる土壌を作る。
        position: "既存実務の尊重・包含"
        speaker: "（Ｅ）委員"
        context: "民間サービスの競争を阻害しない定義の必要性"
      - id: "chunk_014"
        source_doc_id: "20210414diji01_minutes.pdf"
        source_filename: "20210414diji01_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/790/20210414digi01_minutes.pdf"
        source_date: "2021-04-14"
        verbatim_quote: |
          先ほどご指摘いただきましたとおり、こちらも現状の確認が必要だということ
          は理解しまして、今後の課題とさせていただきます。
        position: "既存実務の尊重・包含"
        speaker: "（Ｂ）委員"
        context: "規約ベースの電子的な取り扱いについても現状確認が必要であることの認識"
      - id: "chunk_015"
        source_doc_id: "20210531diji02_minutes.pdf"
        source_filename: "20210531diji02_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/799/20210531diji02_minutes.pdf"
        source_date: "2021-05-31"
        verbatim_quote: |
          （Ｅ） 実務にあるかぎかっこ付き電子船荷証券なるものを、実務は船荷証券だと思っているということです。難しい議論はあえて抜きにして、今国際PIグループが六つか七つ承認している、それが電子船荷証券なのだという、それはもう理屈の世界ではなくてそういうものだと思っているというご認識は持っていただいて、最終的に出来上がった立法が恐らくそれら既に実務にあるもの、あるいはこれから作られよとするものに影響があるものだという前提になっていると思います。その上でこれは第 1 回の繰り返しですが、過剰な規制によって、あるいは必ずしも合理的でない選別が加わることによって、これは電子船荷証券、これは電子船荷証券ではないと選別をする形になるというのは望ましくないであろうと思います。
        position: "既存実務の尊重・包含"
        speaker: "（Ｅ）委員"
        context: "実務上の認識に基づき、既存スキームを排除しない立法を求める意見"
      - id: "chunk_016"
        source_doc_id: "20210531diji02_minutes.pdf"
        source_filename: "20210531diji02_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/799/20210531diji02_minutes.pdf"
        source_date: "2021-05-31"
        verbatim_quote: |
          （Ｄ） いわゆるBOLERO のようなものに法的な裏付けというのは、おっしゃったような物権的効力を与えるということがあり得るのかというところを問題提起しています。また、どういったものに主眼を置くのかといったところについては、第 1 回のご議論を踏まえて、 いわゆるBOLERO のようなものを取り込むというところがメインなのか、それとは全く別次元のものが日本法によって手当てされることによって流通していくというようなことをイメージするのかといったような意味合いでご提案したもので、
        position: "既存実務の取り込み重視"
        speaker: "（Ｄ）委員"
        context: "制度設計の論点設定（BOLEROへの法的位置づけと新規立法の関係）"
      - id: "chunk_017"
        source_doc_id: "20210702diji03_material.pdf"
        source_filename: "20210702diji03_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/802/20210702diji03_material.pdf"
        source_date: "2021-07-02"
        verbatim_quote: |
          【甲案】 船荷証券に記載すべき事項が記録された電磁的記録について，船荷証
          券そのものではないとする考え方（注１）
          （注１）船荷証券に記載すべき事項が電磁的方法によって提供された場合におい
          て，その電磁的記録を船荷証券と機能的に同等であるとする方向で規律を
          設けることなどが考えられる。
        position: "甲案派"
        speaker: null
        context: "甲案の定義"
      - id: "chunk_018"
        source_doc_id: "20210702diji03_material.pdf"
        source_filename: "20210702diji03_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/802/20210702diji03_material.pdf"
        source_date: "2021-07-02"
        verbatim_quote: |
          【乙案】 電磁的方法による船荷証券の発行等を可能とする考え方（注５）
          （注５）船荷証券に関する法律行為の方式として，電磁的方法による交付，裏書
          等を認める旨の規律を設けることなどが考えられる。
        position: "乙案派"
        speaker: null
        context: "乙案の定義"
      - id: "chunk_019"
        source_doc_id: "20210819diji04_material.pdf"
        source_filename: "20210819diji04_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/812/20210819diji04_material.pdf"
        source_date: "2021-08-19"
        verbatim_quote: |
          ○ 電子化を検討する場合の方向性について、どのように考えるか。
          【①案】 電磁的記録を商法上の「船荷証券」並びに民法上の「物」及び「有価
          証券」とする考え方。
          【②案】 電磁的記録に対する排他的な「支配」といった新たな概念を創出し，
          「支配」の移転に紙の船荷証券の裏書と同一の効力を認めるとするなど
          して，紙の船荷証券と同等の効力を認める方向で検討する考え方。
          【③案】 運送品の引渡しに係る債権の移転という実体面に着目し，電磁的記録
          の移転を債権譲渡の効力要件かつ対抗要件とするなどして，紙の船荷
          証券が発行されている場合と同等の法律関係を形成する方向で検討する考
          え方。
        position: "両論併記"
        speaker: null
        context: "法的性質に関する3つの主要案の提示"
      - id: "chunk_020"
        source_doc_id: "20210819diji04_material.pdf"
        source_filename: "20210819diji04_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/812/20210819diji04_material.pdf"
        source_date: "2021-08-19"
        verbatim_quote: |
          ⑴ ①案に立った場合
          民法上の「物」であるとされるため，商法の船荷証券に関する規定はもちろんのこと，民法の有価
          証券に関する規定が適用されることに加え，留置権や質権といった物権の客
          体にもなることとなる。もっとも，民法上の「物」の概念を拡張すること
          については，我が国の法体系に大きな影響を及ぼすこととなるため，その
          必要性も含め，慎重に検討する必要がある。
        position: "①案支持（物権的効力重視）"
        speaker: null
        context: "①案のメリットと慎重論"
      - id: "chunk_021"
        source_doc_id: "20210819diji04_material.pdf"
        source_filename: "20210819diji04_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/812/20210819diji04_material.pdf"
        source_date: "2021-08-19"
        verbatim_quote: |
          ⑶ ③案は，①案や②案とは異なり，電磁的記録の発生や移転という側面で
          はなく，運送品の引渡しに係る債権の移転という実体面に着目し，電磁的
          記録の移転を債権譲渡の効力要件かつ対抗要件とするなどして，その結果
          として，紙の船荷証券が発行されている場合と同等の法律関係を形成しよ
          うとするものである。譲渡記録が電子記録債権の譲渡の効力要件であると
          する電子記録債権法や，振替口座簿の記録の変更が振替株式の譲渡の効力
          要件であるとする社債，株式等の振替に関する法律の考え方と親和的で
          ある。
        position: "③案支持（債権譲渡に着目）"
        speaker: null
        context: "③案の概要と親和性の高い既存法"
      - id: "chunk_022"
        source_doc_id: "20211027diji06_material.pdf"
        source_filename: "20211027diji06_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/824/20211027diji06_material.pdf"
        source_date: "2021-10-27"
        verbatim_quote: |
          【①案】 電磁的船荷証券記録に対する排他的な「支配」といった新たな概念を
          創出した上で，電磁的船荷証券記録に紙の船荷証券と同一の効力を認
          めるとするなどして，紙の船荷証券と同等の効力を認める方向で検討
          する考え方。
        position: "①案支持（機能的同等性重視）"
        speaker: "（J）"
        context: "①案の定義"
      - id: "chunk_023"
        source_doc_id: "20211027diji06_material.pdf"
        source_filename: "20211027diji06_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/824/20211027diji06_material.pdf"
        source_date: "2021-10-27"
        verbatim_quote: |
          【②案】 運送品の引渡しに係る債権の移転という実体面に着目し，電磁的記録
          の移転を債権譲渡の効力要件かつ対抗要件とするなどして，紙の船荷
          証券が発行されている場合と同等の法律関係を形成する方向で検討す
          る考え方。
        position: "②案支持（債権譲渡構成）"
        speaker: null
        context: "②案の基本構成"
      - id: "chunk_024"
        source_doc_id: "20211027diji06_material.pdf"
        source_filename: "20211027diji06_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/824/20211027diji06_material.pdf"
        source_date: "2021-10-27"
        verbatim_quote: |
          なお，研究会資料４においては，電磁的記録を商法上の「船荷証券」並び
          に民法上の「物」及び「有価証券」とする考え方（研究会資料４第３の２の①案）も提示していたが，民法上の「物」の概念を拡張するなど我が国の法体系に大きな影響を及ぼすこととなるため，このような考え方を採用することは困難であると考えられる。
        position: null
        speaker: null
        context: "採用困難な構成についての言及"
      - id: "chunk_025"
        source_doc_id: "20211027diji06_material.pdf"
        source_filename: "20211027diji06_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/824/20211027diji06_material.pdf"
        source_date: "2021-10-27"
        verbatim_quote: |
          少なくともそれらと
          親和性があるのは、やはり①案なのではないかと。少なくとも②案のような方向性である
          べき必然性はよく分からないというコメントもありました。
        position: "①案支持（機能的同等性重視）"
        speaker: "（E）"
        context: "①案の方が国際的潮流（MLETR等）と親和性があるとの意見"
      - id: "chunk_026"
        source_doc_id: "20211027diji06_material.pdf"
        source_filename: "20211027diji06_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/824/20211027diji06_material.pdf"
        source_date: "2021-10-27"
        verbatim_quote: |
          本当に①案のやり方で立法させてもらえるかどうかについての不安が、②案
          が出てきている最大の原因だということは前提に、何か困る話があれば教えていただけ
          ればと思います。
        position: "継続検討"
        speaker: "（A）"
        context: "②案がバックアップとして検討されている背景の説明"
      - id: "chunk_027"
        source_doc_id: "20211130digi07_material.pdf"
        source_filename: "20211130digi07_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/830/20211130digi07_material.pdf"
        source_date: "2021-11-30"
        verbatim_quote: |
          もっとも，「船荷証券と同一の効力」としてどのようなものが含まれ
          るのかについては，必ずしも明らかではなく，解釈に委ねられる部分が
          多く残ることが想定される。また，この規定とみなし規定によって，紙の
          船荷証券に適用される規定の一部については電磁的船荷証券記録にも
          当然に適用されることになるということができるが，そうではない
          規定については個別的に規定を置くこととなるため，紙の船荷証券に
          適用される規定については，①電磁的船荷証券記録にも当然に適用さ
          れるものとして特に規定を設けないもの，②電磁的船荷証券記録に当
          然には適用されないものとして個別的に規定を設けるものに分類され
          るほか，③電磁的船荷証券記録には適用すべきではないものとして規
          定を設けないものもあるため，合計３通りに分類されることになる。
        position: "①案の課題"
        speaker: null
        context: "①案における効力規定の不明確さ"
      - id: "chunk_028"
        source_doc_id: "20211130digi07_material.pdf"
        source_filename: "20211130digi07_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/830/20211130digi07_material.pdf"
        source_date: "2021-11-30"
        verbatim_quote: |
          ②案は，電磁的船荷証券記録の支配の移転を運送品の引渡しに係る債権の譲
          渡の効力要件及び対抗要件とするなどして，紙の船荷証券が発行され
          ている場合と同等の法律関係を形成する方向で検討する考え方である。②案に
          立つ場合には，電磁的船荷証券記録の支配の移転そのものに何らかの法的効果
          が当然に付与されるわけではなく，まずは，電磁的船荷証券記録の支配の移転
          等を運送品の引渡しに係る債権の移転又はこれを目的とする質権の設定の効
          力要件とすることになる。
        position: "②案の構成"
        speaker: null
        context: "②案の基本構成"
      - id: "chunk_029"
        source_doc_id: "20211130digi07_material.pdf"
        source_filename: "20211130digi07_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/830/20211130digi07_material.pdf"
        source_date: "2021-11-30"
        verbatim_quote: |
          本文においては，紙の船荷証券に適用される規定のうち電磁的船荷証
          券記録にも適用すべきものについては全て規定を設ける方向で検討
          することを試みることとしている。
        position: "継続検討"
        speaker: null
        context: "①案採用時の個別規定化の方針"
      - id: "chunk_030"
        source_doc_id: "20220119digi08_material.pdf"
        source_filename: "20220119digi08_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/835/20220119digi08_material.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          【Ａ案】 指図証券型を規律せずに裏書禁止型とそれ以外の２類型のみとする
          考え方。
          【Ｂ案】 ４類型をそのまま維持する考え方。
          【Ｃ案】 記名式所持人払証券型と無記名証券型を規律せずに指図証券型と裏
          書禁止型の２類型のみとする考え方。
        position: "継続検討"
        speaker: null
        context: "類型に関する3つの案の提示"
      - id: "chunk_031"
        source_doc_id: "20220119digi08_material.pdf"
        source_filename: "20220119digi08_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/835/20220119digi08_material.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          Ａ案は，指図証券型を規律しないというものではあるが，そ
          のことは指図証券型を否定することを意味するものではなく，むしろ，電磁
          的船荷証券記録の方式に関する規律を単純化することにより，多くのシス
          テムが利用できるようにすることを目指すものである。
        position: "A案支持の論拠"
        speaker: null
        context: "A案の趣旨説明"
      - id: "chunk_032"
        source_doc_id: "20220119digi08_material.pdf"
        source_filename: "20220119digi08_material.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/835/20220119digi08_material.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          ４ Ｃ案について
          Ｃ案は，②記名式所持人払証券型と④無記名証券型を規律せずに②記名式
          所持人払証券と④無記名証券については，ほとんど利用されていないという
          実情を考慮したものであるが，利用されていないとはいえ，それらの
          ついての規定が存在するのであるし，電子化する場合であっても，理論上は
          ②記名式所持人払証券型と④無記名証券型を観念することができるのであ
          るから，Ｃ案の採否については慎重に検討する必要があるように思われる。
        position: "B案支持の論拠"
        speaker: null
        context: "C案に対する慎重論"
      - id: "chunk_033"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          C 案は実務上ほぼ利用されていない記名式所持人払証券型と無記名証券型については規律せずに指図証券型と裏書禁止型の 2 類型のみを規律するという考え方です。
        position: "継続検討"
        speaker: "（Ｂ）"
        context: "A案、B案、C案の提示と概要説明"
      - id: "chunk_034"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案と B 案については、二つの次元の異なる意見がありました。一つ目は、A 案は、実
          際には指図式 B/L 的なものが多く出回っている点からすると、不自然な感じは確かにする
          のですが、この補足説明を読むと、法律上の一番概括的なというか、最低限の要求として
          この 2 種類があるようにすべしというだけであって、別途、規約でプラスアルファの要件
          を設定して、つまり単に支配を移転するというだけではなくて、プラス、システムによっ
          ては裏書ということも選ぶこともできて、その場合は裏書付きではないと移転もできない
          という規約を設定すれば、それにみんなが合意するのであれば、それの効力を否定する
          趣旨ではないということだから、語弊を恐れずに言えばA 案でも意外といけるのではないか
          みたいなコメントをもらっていて、 私も意外とそうなのかもしれないと若干思っています。
        position: "A案支持の論拠"
        speaker: "（Ｄ）"
        context: "A案の理論的側面と実務上の許容可能性についての意見紹介"
      - id: "chunk_035"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_036"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_037"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_038"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_039"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_040"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_041"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_042"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_043"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_044"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_045"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_046"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_047"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_048"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_049"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_050"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_051"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_052"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_053"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_054"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_055"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_056"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_057"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_058"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_059"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_060"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_061"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_062"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_063"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_064"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_065"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_066"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_067"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_068"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_069"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_070"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_071"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_072"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_073"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_074"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_075"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_076"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_077"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_078"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_079"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_080"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_081"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_082"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_083"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_084"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_085"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_086"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_087"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_088"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_089"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_090"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_091"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_092"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_093"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_094"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_095"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_096"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_097"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_098"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_099"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_100"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_101"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_102"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_103"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_104"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_105"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_106"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_107"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_108"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_109"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_110"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_111"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_112"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_113"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_114"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_115"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_116"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_117"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_118"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_119"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_120"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_121"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_122"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_123"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_124"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_125"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_126"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_127"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_128"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_129"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_130"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_131"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_132"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_133"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_134"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_135"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_136"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_137"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_138"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_139"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_140"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_141"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_142"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_143"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_144"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_145"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_146"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_147"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_148"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_149"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_150"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_151"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_152"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_153"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_154"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_155"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_156"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_157"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_158"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_159"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_160"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_161"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_162"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_163"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_164"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_165"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_166"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_167"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_168"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_169"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_170"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_171"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_172"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_173"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_174"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_175"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_176"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_177"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_178"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_179"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_180"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_181"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_182"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_183"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_184"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_185"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_186"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_187"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_188"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_189"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_190"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_191"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_192"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_193"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_194"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_195"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_196"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_197"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_198"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_199"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_200"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_201"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_202"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_203"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_204"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_205"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_206"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_207"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_208"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_209"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_210"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_211"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_212"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_213"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_214"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_215"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_216"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_217"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_218"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_219"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_220"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_221"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_222"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_223"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_224"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_225"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_226"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_227"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_228"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_229"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_230"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_231"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_232"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_233"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_234"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_235"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_236"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_237"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_238"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_239"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_240"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_241"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_242"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_243"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_244"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_245"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_246"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_247"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_248"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_249"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_250"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_251"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_252"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_253"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_254"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_255"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_256"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_257"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_258"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_259"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_260"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_261"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_262"
        source_doc_id: "20220119digi08_minutes.pdf"
        source_filename: "20220119digi08_minutes.pdf"
        source_url: "https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf"
        source_date: "2022-01-19"
        verbatim_quote: |
          A 案を採用した場合には、 電磁的船荷証券記録については、 譲渡が禁止されるものを除き、
          それに関する権限を譲渡するには電磁的船荷証券記録の支配の移転をもって足りるとする
          ことにより、制度としては比較的単純で分かりやすいものとなります。
        position: "A案支持の論拠"
        speaker: "（Ｂ）"
        context: "A案のメリット説明"
      - id: "chunk_263"

---

# 出典一覧

## 審議会資料

| ID | 資料名 | 審議会/出典 | URL |
|----|--------|-------------|-----|
| D001 | 船荷証券に関する規定等の見直しにおける検討事項の例 | 法務省：法制審議会商法（船荷証券等関係）部会第１回会議（令和４年４月２７日開催） | [リンク](https://www.moj.go.jp/content/001373713.pdf) |
| D002 | 参考資料２－２　イギリス法における電子船荷証券に係る論点とLaw Commissionの立場 | 法務省：法制審議会商法（船荷証券等関係）部会第２回会議（令和４年６月１５日開催） | [リンク](https://www.moj.go.jp/content/001375177.pdf) |
| D003 | 部会資料２　船荷証券に関する規定等の見直しに関する論点の検討（１） | 法務省：法制審議会商法（船荷証券等関係）部会第２回会議（令和４年６月１５日開催） | [リンク](https://www.moj.go.jp/content/001375189.pdf) |
| D004 | 部会資料３　船荷証券に関する規定等の見直しに関する論点の検討（２）【PDF】 | 法務省：法制審議会商法（船荷証券等関係）部会第３回会議（令和４年７月２７日開催） | [リンク](https://www.moj.go.jp/content/001377877.pdf) |
| D005 | 部会資料４船荷証券に関する規定等の見直しに関する論点の検討（３） | 法務省：法制審議会商法（船荷証券等関係）部会第４回会議（令和４年８月３１日開催） | [リンク](https://www.moj.go.jp/content/001379859.pdf) |
| D006 | 部会資料５船荷証券に関する規定等の見直しに関する論点の検討（４） | 法務省：法制審議会商法（船荷証券等関係）部会第５回会議（令和４年１０月１２日開催） | [リンク](https://www.moj.go.jp/content/001382224.pdf) |
| D007 | 部会資料６船荷証券に関する規定等の見直しに関する論点の検討（５） | 法務省：法制審議会商法（船荷証券等関係）部会第６回会議（令和４年１１月３０日開催） | [リンク](https://www.moj.go.jp/content/001385305.pdf) |
| D008 | 船荷証券に関する規定等の見直しに関する中間試案のたたき台 | 法務省：法制審議会商法（船荷証券等関係）部会第７回会議（令和５年１月２５日開催） | [リンク](https://www.moj.go.jp/content/001390064.pdf) |
| D009 | 部会資料８　船荷証券に関する規定等の見直しに関する中間試案のたたき台(2) | 法務省：法制審議会商法（船荷証券等関係）部会第８回会議（令和５年３月８日開催） | [リンク](https://www.moj.go.jp/content/001393794.pdf) |
| D010 | 船荷証券に関する規定等の見直しに関する中間試案 | 法務省：「船荷証券に関する規定等の見直しに関する中間試案」（令和５年３月８日）の取りまとめ | [リンク](https://www.moj.go.jp/content/001394826.pdf) |
| D011 | 船荷証券に関する規定等の見直しに関する中間試案の補足説明 | 法務省：「船荷証券に関する規定等の見直しに関する中間試案」（令和５年３月８日）の取りまとめ | [リンク](https://www.moj.go.jp/content/001394827.pdf) |
| D012 | 【参考資料】MLETR対照表（「船荷証券に関する規定等の見直しに関する中間試案の補足説明」の参考資料） | 法務省：「船荷証券に関する規定等の見直しに関する中間試案」（令和５年３月８日）の取りまとめ | [リンク](https://www.moj.go.jp/content/001394829.pdf) |
| D013 | 部会資料１０　「船荷証券に関する規定等の見直しに関する中間試案」に対して寄せられた意見の概要等 | 法務省：法制審議会商法（船荷証券等関係）部会第１０回会議（令和５年５月３１日開催） | [リンク](https://www.moj.go.jp/content/001397730.pdf) |
| D014 | 部会資料１１　船荷証券に関する規定等の見直しに関する要綱案のとりまとめに向けた検討 | 法務省：法制審議会商法（船荷証券等関係）部会第１１回会議（令和５年８月３０日開催） | [リンク](https://www.moj.go.jp/content/001402989.pdf) |
| D015 | 部会資料１２　船荷証券に関する規定等の見直しに関する要綱案のとりまとめに向けた検討（２） | 法務省：法制審議会商法（船荷証券等関係）部会第１２回会議（令和５年１０月４日開催） | [リンク](https://www.moj.go.jp/content/001404064.pdf) |
| D016 | 商法（船荷証券等関係）部会名簿 | 法務省：法制審議会－商法（船荷証券等関係）部会 | [リンク](https://www.moj.go.jp/content/001408123.pdf) |
| D017 | 部会資料１３　船荷証券に関する規定等の見直しに関する要綱案のとりまとめに向けた検討（３） | 法務省：法制審議会商法（船荷証券等関係）部会第１３回会議（令和６年１月２４日開催） | [リンク](https://www.moj.go.jp/content/001411003.pdf) |
| D018 | 部会資料１４　船荷証券に関する規定等の見直しに関する要綱案のとりまとめに向けた検討（４） | 法務省：法制審議会商法（船荷証券等関係）部会第１４回会議（令和６年４月１７日開催） | [リンク](https://www.moj.go.jp/content/001417519.pdf) |
| D019 | 部会資料１５　商法（船荷証券等関係）等の改正に関する要綱案のたたき台 | 法務省：法制審議会商法（船荷証券等関係）部会第１５回会議（令和６年７月２４日開催） | [リンク](https://www.moj.go.jp/content/001422019.pdf) |
| D020 | 部会資料１６－１ 商法（船荷証券等関係）等の改正に関する要綱案 | 法務省：法制審議会商法（船荷証券等関係）部会第１６回会議（令和６年８月２１日開催） | [リンク](https://www.moj.go.jp/content/001423391.pdf) |
| D021 | 第1回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/790/20210414digi01_minutes.pdf) |
| D022 | 第1回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/779/20210414diji01_agenda.pdf) |
| D023 | 第1回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/780/20210414diji01_catalog.pdf) |
| D024 | 資料1 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/781/20210414diji01_material.pdf) |
| D025 | 第1回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/789/20210414diji01_member.pdf) |
| D026 | 別紙1 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/782/20210414diji01_ss1.pdf) |
| D027 | 別紙2 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/783/20210414diji01_ss2.pdf) |
| D028 | 別紙3 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/784/20210414diji01_ss3.pdf) |
| D029 | 別紙4 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/785/20210414diji01_ss4.pdf) |
| D030 | 別紙5 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/786/20210414diji01_ss5.pdf) |
| D031 | 別紙6 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/787/20210414diji01_ss6.pdf) |
| D032 | 別紙7 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/788/20210414diji01_ss7.pdf) |
| D033 | 第2回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/791/20210531diji02_agenda.pdf) |
| D034 | 第2回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/792/20210531diji02_catalog.pdf) |
| D035 | 資料2 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/793/20210531diji02_material.pdf) |
| D036 | 第2回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/798/20210531diji02_member.pdf) |
| D037 | 第2回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/799/20210531diji02_minutes.pdf) |
| D038 | 参考資料1 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/797/20210531diji02_referance.pdf) |
| D039 | 別紙10 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/796/20210531diji02_ss10.pdf) |
| D040 | 別紙8 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/794/20210531diji02_ss8.pdf) |
| D041 | 別紙9 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/795/20210531diji02_ss9.pdf) |
| D042 | 第3回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/800/20210702diji03_agenda.pdf) |
| D043 | 第3回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/801/20210702diji03_catalog.pdf) |
| D044 | 資料3 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/802/20210702diji03_material.pdf) |
| D045 | 第3回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/806/20210702diji03_member.pdf) |
| D046 | 第3回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/807/20210702diji03_mimutes.pdf) |
| D047 | 参考資料3-2 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/805/20210702diji03_reference2.pdf) |
| D048 | 別紙11 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/803/20210702diji03_ss11.pdf) |
| D049 | 別紙12 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/804/20210702diji03_ss12.pdf) |
| D050 | 第4回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/810/20210819diji04_agenda.pdf) |
| D051 | 第4回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/811/20210819diji04_catalog.pdf) |
| D052 | 資料4 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/812/20210819diji04_material.pdf) |
| D053 | 第4回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/814/20210819diji04_member.pdf) |
| D054 | 第4回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/815/20210819diji04_minutes.pdf) |
| D055 | 別紙13 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/813/20210819diji04_ss13.pdf) |
| D056 | 第5回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/816/20210921diji05_agenda.pdf) |
| D057 | 第5回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/817/20210921diji05_catalog.pdf) |
| D058 | 資料5 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/818/20210921diji05_material.pdf) |
| D059 | 第5回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/820/20210921diji05_member.pdf) |
| D060 | 第5回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/821/20210921diji05_minutes.pdf) |
| D061 | 別紙15 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/819/20210921diji05_ss15.pdf) |
| D062 | 第6回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/822/20211027diji06_agenda.pdf) |
| D063 | 第6回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/823/20211027diji06_catalog.pdf) |
| D064 | 資料6 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/824/20211027diji06_material.pdf) |
| D065 | 第6回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/826/20211027diji06_member.pdf) |
| D066 | 第6回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/827/20211027diji06_minutes.pdf) |
| D067 | 別紙16 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/825/20211027diji06_ss16.pdf) |
| D068 | 第7回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/828/20211130digi07_agenda.pdf) |
| D069 | 第7回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/829/20211130digi07_catalog.pdf) |
| D070 | 資料7 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/830/20211130digi07_material.pdf) |
| D071 | 第7回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/831/20211130digi07_member.pdf) |
| D072 | 第7回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/832/20211130digi07_minutes.pdf) |
| D073 | 第8回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/833/20220119digi08_agenda.pdf) |
| D074 | 第8回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/834/20220119digi08_catalog.pdf) |
| D075 | 資料8 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/835/20220119digi08_material.pdf) |
| D076 | 第8回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/837/20220119digi08_member.pdf) |
| D077 | 第8回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/838/20220119digi08_minutes.pdf) |
| D078 | 別紙17 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/836/20220119digi08_ss17.pdf) |
| D079 | 第9回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/839/20220222digi09_agenda.pdf) |
| D080 | 第9回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/840/20220222digi09_catalog.pdf) |
| D081 | 第9回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/841/20220222digi09_member.pdf) |
| D082 | 第9回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/842/20220222digi09_minutes.pdf) |
| D083 | 第10回議事次第 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/843/20220323digi10_agenda.pdf) |
| D084 | 第10回配付資料目録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/844/20220323digi10_catalog.pdf) |
| D085 | 第10回出席者名簿 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/845/20220323digi10_member.pdf) |
| D086 | 第10回議事録 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/846/20220323digi10_minutes.pdf) |
| D087 | metadata_moj.go.jp_20251208_180730.json | - | - |
| D088 | metadata_shojihomu.or.jp_20251208_175118.json | - | - |
| D089 | README.md | - | - |
| D090 | 商事法の電子化に関する研究会報告書－船荷証券の電子化について－ | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/847/report.pdf) |
| D091 | 別添資料 | 公益社団法人 商事法務研究会  | 商事法の電子化に関する研究会（船荷証券） | [リンク](https://www.shojihomu.or.jp/public/library/848/sv.pdf) |


---

# 処理メタデータ

**分析フォーカス**: 電子船荷証券

## データソース

| 種別 | パス | 件数 |
|------|------|------|
| 審議会資料 | `each_project\funani\shingikai` | 91 ファイル |

## 処理パイプライン: 事前仮説生成 (pre_hypothesis_iterative)

### Part 1 (Map)
- **フェーズ**: 論点抽出
- **入力**: 91 → **出力**: 91
- **モデル**: `gemini-flash-lite-latest`
- **詳細**: 並列10ワーカー

### Part 2 (Tree Reduce)
- **フェーズ**: Q&A統合
- **入力**: 10 → **出力**: 1
- **モデル**: `gemini-flash-lite-latest`
- **詳細**: 4レベル並列

## ツリーReduce統計

- 初期バッチ数: 10
- 並列レベル数: 4
- レベル詳細: L1:5ペア → L2:3ペア → L3:2ペア → L4:1ペア


*生成日時: 2025-12-16 11:52:35*


---
# 実験メタ情報
- 実行日時: 2025-12-16 11:52:35
- モード: pre_hypothesis_iterative (2段階自動実行)
- モデル: gemini-flash-lite-latest
- 温度: 0.0
- max_output_tokens: 64000
- top_p: 0.95
- top_k: 40
- セッション数: 91
---
