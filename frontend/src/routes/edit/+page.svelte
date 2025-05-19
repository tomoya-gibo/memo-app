<script>
  import { memoData } from "$lib/stores/dataStore";
  import InputScreen from "$lib/components/InputScreen.svelte";
  import { goto } from "$app/navigation";

  /*
  入力フォームの初期値を取得するため、
  memoData(store)のそれぞれの値にアクセスする。
  */
  let title = $memoData.title;
  let body = $memoData.body;
  let references = $memoData.references;
  
  function updateData(inputData) {
    memoData.set(inputData);

    goto("/detail");

    // デバッグ用
    console.log(inputData.title, inputData.body, inputData.references);
    
  };

  // デバッグ用
  console.log(title, body, references);
  
</script>

<InputScreen
  {title}
  {body}
  {references}
  onSave={updateData}
/>