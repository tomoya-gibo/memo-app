export async function fetchData(url) {
  const res = await fetch(url);
  console.log("res:", res);
  const datas = await res.json();
  console.log("datas:", datas);

  return datas;
}