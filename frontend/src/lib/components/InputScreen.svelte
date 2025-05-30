<script>
  import { memoData } from "$lib/stores/dataStore";
  import { onMount } from "svelte";
  
  export let title;
  export let body;
  export let references;

  // 保存を実行するイベントハンドラを受け取る
  export let onSave;

  //console.log("inputData:", inputData);
  
  onMount(() => console.log("b"));

</script>

<div class="input">
  <p>タイトル：</p>
  <input type="text" name="title" bind:value={title}>

  <p>本文：</p>
  <input type="text" name="body" bind:value={body}>

  <p>参考文献：</p>
  <input type="text" name="references" bind:value={references}>
</div>

<button on:click={() => onSave(title, body, references)}>保存</button>