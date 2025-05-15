<script>
  import { memoData } from "$lib/stores/dataStore";
  import { onMount } from "svelte";
  
  let title = "";
  let body = "";
  let references = "";

  onMount(() => {
    const unsubscribe = memoData.subscribe(value => {
      // valueはオブジェクトの配列で与えられる。
      /*
      TODO： ページごとに対応したオブジェクトにアクセスできるようにする。
      例： "テスト1"をクリックするとテスト1の詳細な中身が、
      "テスト2"をクリックするとテスト2の詳細な中身が表示される。
      */
      title = value[0].title;
      body = value[0].body;
      references = value[0].references;
    });
    return () => {
      unsubscribe();
    }
  });
  
</script>

<div class="detail">
  <h1>タイトル：{title}</h1>
  <p>{body}</p>
  <h2>参考文献：</h2>
  <p>{references}</p>
</div>