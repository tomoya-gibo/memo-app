<script>
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";
  import { fetchData } from "$lib/api/fetchData";
  
  let title = "";
  let body = "";
  let references = "";


  // バックエンドからデータを取得して各変数に代入する関数
  async function fetchSetData() {
    const fetchedData = await fetchData();
    title = fetchedData.title;
    body = fetchedData.body;
    references = fetchedData.references;

    await console.log("detailでのset後の各データ", title, body, references);
  }

  onMount(() => {
    fetchSetData();
  });

  function goToHome() {
    console.log("detailのgoToHome内での値", title, body, references);
    
    goto("/home");
  }
  
</script>

<div class="detail">
  <h1>タイトル：{title}</h1>
  <p>{body}</p>
  <h2>参考文献：</h2>
  <p>{references}</p>
  <button on:click={goToHome}>メモ一覧に戻る</button>
  <a href="/edit"><button>編集する</button></a>
</div>