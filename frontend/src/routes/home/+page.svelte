<script>
  import { memoData } from "$lib/stores/dataStore";
  import { onMount } from "svelte";

  // サンプルデータ
  const sampleDatas = {
      title: "テスト1",
      body: "テスト1の本文",
      references: "テスト1の参考文献"
    };

  let datas = {};

  /*if (Object.keys(datas).length === 0) {
    memoData.set(sampleDatas);
    console.log(datas);
    
    //datas = sampleDatas;
  };*/

  onMount(() => {
    console.log("onMountの直後のdatas:", datas);
    
    console.log(Object.keys(datas).length);
    
    // datasが空の場合はサンプルデータを初期値として適用。
    if (datas.constructor === Object && Object.keys(datas).length === 0) {
      memoData.set(sampleDatas);
      //datas = sampleDatas;
    } else {
      unsubscribe();
    }

    const unsubscribe = memoData.subscribe((value) => {
      datas = value;
    });
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