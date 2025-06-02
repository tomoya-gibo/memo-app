<script>
  import { memoData } from "$lib/stores/dataStore";
  import InputScreen from "$lib/components/InputScreen.svelte";
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";
  import { fetchData } from "$lib/api/fetchData";

  /*
  入力フォームの初期値を取得するため、
  memoData(store)のそれぞれの値にアクセスする。
  */
  let datas = {
    title: $memoData.title,
    body: $memoData.body,
    references: $memoData.references
  }

  async function fetchSetData() {
    const fetchedData = await fetchData();
    memoData.set(fetchedData);
    console.log("editでset後のdatas",datas);
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
    memoData.set(inputData);
    postData(inputData);

    goto("/detail");

    // デバッグ用
    //console.log(inputData.title, inputData.body, inputData.references);
    
  };

  onMount(() => {
    const unsubscribe = memoData.subscribe((value) => {
      console.log("editのsubscribeの中");
      
      datas = value;
      console.log("editのsubscribe後のdatas", datas);
    });

    console.log("a");
    
    if(!datas.title) {
      console.log("editのifブロックの中");
      fetchSetData();
      //const fetchedData = await fetchData();
      //memoData.set(fetchedData);
      console.log("onMount内のeditのdatas", datas);
      
    }

    return () => {
      unsubscribe();
    }
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