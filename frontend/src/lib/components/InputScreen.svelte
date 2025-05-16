<script>
  import { memoData } from "$lib/stores/dataStore";
  
  export let title;
  export let body;
  export let references;

  //保存を実行するイベントハンドラ
  export let onSave;
</script>

<div class="input">
  <p>タイトル：</p>
  <input type="text" name="title" value={title}>

  <p>本文：</p>
  <input type="text" name="body" value={body}>

  <p>参考文献：</p>
  <input type="text" name="references" value={references}>
</div>

<button on:click={onSave}>保存</button>