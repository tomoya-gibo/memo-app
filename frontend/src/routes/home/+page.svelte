<script>
  import { memoData } from "$lib/stores/dataStore";
  import { onMount } from "svelte";

  // サンプルデータ
  const sampleDatas = {
    title: "テスト1",
    body: "テスト1の本文",
    references: "テスト1の参考文献"
  };

  let title = $memoData.title;
  let body = $memoData.body;
  let references = $memoData.references;
  
  let datas = {
    title: title,
    body: body,
    references: references
  };

  // storeの値が初期値(空文字)かを判定する。空文字であればtrueを返す。
  function isEmpty(obj) {
    return !obj.title || !obj.body || !obj.references;
  }

  console.log("isEmpty:", isEmpty(datas));
  
  console.log("datas定義後の値:", datas);
  
  onMount(() => {
    console.log("onMountの先頭でのdatas:", datas);
    
    console.log("datasのプロパティの個数(onMount直後):", Object.keys(datas).length);

    // store値が初期値の場合はサンプルデータを初期値として適用。
    if (isEmpty(datas)) {
      console.log("ifブロックの中");
      
      memoData.set(sampleDatas);

      console.log("set後のdatasの値", datas);
    }
    
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