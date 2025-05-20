<script>
  import { memoData } from "$lib/stores/dataStore";
  import { onMount } from "svelte";

  // サンプルデータ
  const sampleDatas = {
      title: "テスト1",
      body: "テスト1の本文",
      references: "テスト1の参考文献"
    };

  /*let title = "";
  let body = "";
  let references = "";
  */
  let datas = sampleDatas;

  /*if (datas.constructor === Object && Object.keys(datas).length === 0) {
    memoData.set(sampleDatas)
    //datas = sampleDatas;
    console.log(datas);
  }*/

  onMount(() => {
    console.log("onMountの先頭でのdatas:", datas);
    
    console.log(Object.keys(datas).length);

    const unsubscribe = memoData.subscribe((value) => {
      /*title = value.title;
      body = value.body;
      references = value.references;*/
      datas = value;
    });

    // datasが空の場合はサンプルデータを初期値として適用。
    /*if (Object.keys(datas).length === 0) {
      memoData.set(sampleDatas);
      //datas = sampleDatas;
      console.log(datas);      
    }*/

    return () => {
      unsubscribe();
      // デバッグ用
      console.log(datas);
      console.log(typeof datas);
    }
  });
  //console.log("subscribeされた各データの値:", title, body, references);
  console.log("onMount後のdatas:", datas);
  
  
</script>

<div class="home">
  <h1>メモタイトル一覧</h1>
    <li><a href="/detail">{datas.title}</a></li>
</div>