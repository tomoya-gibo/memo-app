<script>
  import { memoData } from "$lib/stores/dataStore";
    import { onMount } from "svelte";
  
  export let title;
  export let body;
  export let references;

  // 保存を実行するイベントハンドラを受け取る
  export let onSave;

  /*
  /detailのsubscribeで受け取るvalueの型がオブジェクトを想定しているため、
  ユーザから受け取った入力をオブジェクトに変換する。
  */
  let inputData = {
    title: title,
    body: body,
    references: references
  }

  console.log("inputData:", inputData);
  
  onMount(() => console.log("b"));

</script>

<div class="input">
  <p>タイトル：</p>
  <input type="text" name="title" bind:value={inputData.title}>

  <p>本文：</p>
  <input type="text" name="body" bind:value={inputData.body}>

  <p>参考文献：</p>
  <input type="text" name="references" bind:value={inputData.references}>
</div>

<button on:click={() => onSave(inputData)}>保存</button>