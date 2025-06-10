<script>
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";
  import { fetchData } from "$lib/api/fetchData";
  import { page } from "$app/state";
  
  let title = "";
  let body = "";
  let references = "";
  const id = page.url.searchParams.get("id");

  // バックエンドからデータを取得して各変数に代入する関数
  async function fetchSetData() {
    console.log("受け取ったid:", id);
    
    // クリックしたデータのidに紐づいたデータを取得し、各要素に代入
    const fetchUrl = "http://localhost:8000/detail/" + id;
    const fetchedData = await fetchData(fetchUrl);
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