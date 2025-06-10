<script>
  import InputScreen from "$lib/components/InputScreen.svelte";
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";
  import { fetchData } from "$lib/api/fetchData";
  import { page } from "$app/state";

  let datas = {
    title: "",
    body: "",
    references: ""
  }

  const id = page.url.searchParams.get("id");

  async function fetchSetData() {
    const fetchUrl = "http://localhost:8000/detail/" + id;
    datas = await fetchData(fetchUrl);

    await console.log("editでset後のdatas",datas);
  }

  async function postData(inputData) {
    const response = await fetch("http://localhost:8000/edit/" + id, {
      method: "POST",
      body: JSON.stringify(inputData),
      headers: {
        "Content-Type": "application/json"
      }
    });
    
    console.log("ステータス:", response.status);
  }

  function updateData(title, body, references) {
    let inputData = {
      title: title,
      body: body,
      references: references
    }
    postData(inputData);

    goto(`/detail?id=${id}`);

    // デバッグ用
    //console.log(inputData.title, inputData.body, inputData.references);
    
  };

  onMount(() => {
    console.log("a");
    fetchSetData();
  });

  // デバッグ用
  console.log("editのdatas:", datas);
  
</script>

<InputScreen
  title={datas.title}
  body={datas.body}
  references={datas.references}
  onSave={updateData}
/>