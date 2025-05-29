export async function fetchData() {
  const res = await fetch("http://localhost:8000");
  console.log("res:", res);
  const datas = await res.json();
  console.log("datas:", datas);

  return datas;
}