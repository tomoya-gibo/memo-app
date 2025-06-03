<script>
  import { onMount } from "svelte";
  import { fetchData } from "$lib/api/fetchData";

  let datas = {
    title: "",
    body: "",
    references: ""
  };

  // 非同期が必要な処理だけをまとめて関数化する。
  async function fetchSetData() {
    datas = await fetchData();
    console.log("homeのfetch後のdatas", datas);
  }

  console.log("isEmpty:", isEmpty(datas));
  
  console.log("datas定義後の値:", datas);
  
  onMount(() => {
    console.log("onMountの先頭でのdatas:", datas);
    
    console.log("datasのプロパティの個数(onMount直後):", Object.keys(datas).length);

    console.log("datasのプロパティの個数(subscribe後):", Object.keys(datas).length);
    console.log("subscribe後のdatas:", datas);

    fetchSetData();

    return () => {
      //unsubscribe();
      // デバッグ用
      console.log(datas);
      console.log(typeof datas);
    }
  });

  console.log("onMount後のdatas:", datas);
  
  
</script>

<div class="home">
  <h1>メモタイトル一覧</h1>
    <li><a href="/detail">{datas.title}</a></li>
</div>