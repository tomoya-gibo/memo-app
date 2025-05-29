export async function fetchData(fetchURL) {
  const res = await fetch(fetchURL);
  console.log("res:", res);
  const datas = await res.json();
  console.log("datas:", datas);

  return datas;
}