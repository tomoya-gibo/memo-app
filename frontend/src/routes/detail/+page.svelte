<script>
  import { goto } from "$app/navigation";
  import { memoData } from "$lib/stores/dataStore";
  import { onMount } from "svelte";
  import { fetchData } from "$lib/api/fetchData";
  
  let title = "";
  let body = "";
  let references = "";

  async function fetchSetData() {
    const fetchedData = await fetchData();
    memoData.set(fetchedData);
    await console.log("detailでのset後の各データ", title, body, references);
  }

  onMount(() => {
    const unsubscribe = memoData.subscribe(value => {
      console.log("detailのsubscribeの中");
      
      title = value.title;
      body = value.body;
      references = value.references;
    });

    if (!title) {
      console.log("detailのifブロックの中");
      
      fetchSetData();
    }

    return () => {
      unsubscribe();
    }
  });

  function goToHome() {
    memoData.set({ title: title, body: body, references: references});
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