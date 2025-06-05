<script>
  import InputScreen from "$lib/components/InputScreen.svelte";


  let title = "";
  let body = "";
  let references = "";

  function handleCreateNew(title, body, references) {
    // TODO: 保存して画面を遷移する処理を記述する。
  }
</script>

<InputScreen
  title={title}
  body={body}
  references={references}
  onSave={handleCreateNew}
/>