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
  let datas = {};

  onMount(() => {
    console.log("onMountの先頭でのdatas:", datas);
    
    //console.log(Object.keys(datas).length);

    // datasが空の場合はサンプルデータを初期値として適用。
    if (Object.keys(datas).length === 0) {
      console.log("test");
      
      memoData.set(sampleDatas);
      //datas = sampleDatas;
      //console.log(datas);      
    }
    
    const unsubscribe = memoData.subscribe((value) => {
      /*title = value.title;
      body = value.body;
      references = value.references;*/
      console.log("subscribeの中");
      
      datas = value;
    });

    console.log("datasのプロパティの個数:", Object.keys(datas).length);
    console.log(datas);
    
    return () => {
      unsubscribe();
      // デバッグ用
      console.log(datas);
      console.log(typeof datas);
    }
  });

  console.log("onMount後のdatas:", datas);
  
  
</script>

<div class="home">
  <h1>メモタイトル一覧</h1>
    <li><a href="/detail">{datas.title}</a></li>
</div>