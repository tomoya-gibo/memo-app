<script>
  import InputScreen from "$lib/components/InputScreen.svelte";
  import { goto } from "$app/navigation";

  let title = "";
  let body = "";
  let references = "";

  async function postNewData(inputData) {
    const response = await fetch("http://localhost:8000/new", {
      method: "POST",
      body: JSON.stringify(inputData),
      headers: {
        "Content-Type": "application/json"
      }
    });
  }

  function handleCreateNew(title, body, references) {
    // TODO: 保存して画面を遷移する処理を記述する。
    let inputData = {
      title: title,
      body: body,
      references:references,
      id: 4
    }
    postNewData(inputData);

    goto(`/detail?id=${inputData.id}`);
  }
</script>

<InputScreen
  title={title}
  body={body}
  references={references}
  onSave={handleCreateNew}
/>