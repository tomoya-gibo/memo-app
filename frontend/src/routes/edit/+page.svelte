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
  
  let title = $memoData.title;

  async function fetchSetData() {
    const fetchedData = await fetchData();
    memoData.set(fetchedData);
    console.log("editでset後のdatas",datas);
    
  }

  function updateData(inputData) {
    memoData.set(inputData);

    goto("/detail");

    // デバッグ用
    //console.log(inputData.title, inputData.body, inputData.references);
    
  };

  onMount(() => {
    const unsubscribe = memoData.subscribe((value) => {
      console.log("editのsubscribeの中");
      
      datas = value;
      console.log("editのsubscribe後のdatas", datas);
      title = value.title;
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
<input type="text" bind:value={title}>
<InputScreen
  title={title}
  body={datas.body}
  references={datas.references}
  onSave={updateData}
/>