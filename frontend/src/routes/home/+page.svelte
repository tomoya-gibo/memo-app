<script>
  import { onMount } from "svelte";
  import { fetchData } from "$lib/api/fetchData";

  let datas = [];

  // 非同期が必要な処理だけをまとめて関数化する。
  async function fetchSetData() {
    datas = await fetchData();
    console.log("homeのfetch後のdatas", datas);
  }
  
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
  {#each datas as data}
    <li><a href="/detail">{data.title}</a></li>
  {/each}
  <div class="button">
    <a href="/new"><button>新規作成</button></a>
  </div>
</div>