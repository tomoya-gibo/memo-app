// メモのデータを保存する

import { writable } from "svelte/store";

// サンプルデータ(初期値)
const sampleDatas = {
  title: "テスト1",
  body: "テスト1の本文",
  references: "テスト1の参考文献"
};

export const memoData = writable(sampleDatas);
