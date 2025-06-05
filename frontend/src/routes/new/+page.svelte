<script>
  import InputScreen from "$lib/components/InputScreen.svelte";
  import { goto } from "$app/navigation";

  let title = "";
  let body = "";
  let references = "";

  function handleCreateNew(title, body, references) {
    // TODO: 保存して画面を遷移する処理を記述する。
    goto("/detail");
  }
</script>

<InputScreen
  title={title}
  body={body}
  references={references}
  onSave={handleCreateNew}
/>