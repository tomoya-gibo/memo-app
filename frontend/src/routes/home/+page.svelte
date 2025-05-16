<script>
  import { memoData } from "$lib/stores/dataStore";

  // サンプルデータ
  const sampleDatas = {
      title: "テスト1",
      body: "テスト1の本文",
      references: "テスト1の参考文献"
    };

  let datas = {};

  memoData.subscribe((value) => {
    datas = value;
  });

  memoData.set(sampleDatas);
  
  //サンプルデータがdatasに代入されているかデバッグ
  console.log(datas);
  console.log(typeof datas);
  
</script>

<div class="home">
  <h1>メモタイトル一覧</h1>
    <li><a href="/detail">{datas.title}</a></li>
</div>