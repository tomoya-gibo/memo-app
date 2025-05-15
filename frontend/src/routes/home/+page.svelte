<script>
  import { memoData } from "$lib/stores/dataStore";

  // サンプルデータ
  const sampleDatas = [
    {
      title: "テスト1",
      body: "テスト1の本文",
      references: "テスト1の参考文献1"
    },
    {
      title: "テスト2",
      body: "テスト2の本文",
      references: "テスト2の参考文献1"
    }
  ];

  let datas = [];

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
  {#each datas as data}
    <li><a href="/detail">{data.title}</a></li>
  {/each}
</div>