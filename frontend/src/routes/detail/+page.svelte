<script>
  import { memoData } from "$lib/stores/dataStore";

  console.log(memoData.title);
  
</script>

<div class="detail">
  <h1>タイトル：{memoData.title}</h1>
  <p>{memoData.body}</p>
  <h2>参考文献：</h2>
  <p>{memoData.references}</p>
</div>