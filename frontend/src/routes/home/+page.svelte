<script>
  import { memoData } from "$lib/stores/dataStore";
  import { onMount } from "svelte";

  // サンプルデータ
  const sampleDatas = {
    title: "テスト1",
    body: "テスト1の本文",
    references: "テスト1の参考文献"
  };
  
  let datas = {
    title: $memoData.title,
    body: $memoData.body,
    references: $memoData.references
  };

  // storeのタイトルが初期値(空文字)かを判定する。空文字であればtrueを返す。
  function isEmpty(obj) {
    return !obj.title;
  }

  console.log("isEmpty:", isEmpty(datas));
  
  console.log("datas定義後の値:", datas);
  
  onMount(() => {
    console.log("onMountの先頭でのdatas:", datas);
    
    console.log("datasのプロパティの個数(onMount直後):", Object.keys(datas).length);
    
    const unsubscribe = memoData.subscribe((value) => {
      /*title = value.title;
      body = value.body;
      references = value.references;*/
      console.log("subscribeの中");
      console.log("value:", value);
      
      datas = value;

      console.log("subscribeの中のdatas:", datas);
      
    });

    console.log("datasのプロパティの個数(subscribe後):", Object.keys(datas).length);
    console.log("subscribe後のdatas:", datas);

    /*
    storeのtitleが初期値の場合はサンプルデータを初期値として適用。
    subscribeで変更を購読した後に判定を行う。
    */
    if (isEmpty(datas)) {
      console.log("ifブロックの中");
      
      memoData.set(sampleDatas);

      console.log("set後のdatasの値", datas);
    }

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