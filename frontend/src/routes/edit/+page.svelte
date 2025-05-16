<script>
  import { memoData } from "$lib/stores/dataStore";

  // memoData(store)のそれぞれの値にアクセスする。
  let title = $memoData.title;
  let body = $memoData.body;
  let references = $memoData.references;
  
  function saveData() {
    // TODO: ボタンを押した時に、入力されたメモの内容を保存する処理を記述
  };

  // デバッグ用
  console.log(title, body, references);
  
</script>