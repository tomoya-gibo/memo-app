<script>
  import { goto } from "$app/navigation";
  import { memoData } from "$lib/stores/dataStore";
  import { onMount } from "svelte";
  
  let title = "";
  let body = "";
  let references = "";

  onMount(() => {
    const unsubscribe = memoData.subscribe(value => {
      title = value.title;
      body = value.body;
      references = value.references;
    });
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