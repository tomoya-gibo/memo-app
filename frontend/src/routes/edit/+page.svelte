<script>
  import { memoData } from "$lib/stores/dataStore";
  import InputScreen from "$lib/components/InputScreen.svelte";
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";
  import { fetchData } from "$lib/api/fetchData";


  let datas = {
    title: "",
    body: "",
    references: ""
  }

  async function fetchSetData() {
    datas = await fetchData();

    await console.log("editでset後のdatas",datas);
  }

  async function postData(inputData) {
    const response = await fetch("http://localhost:8000/edit", {
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

    goto("/detail");

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