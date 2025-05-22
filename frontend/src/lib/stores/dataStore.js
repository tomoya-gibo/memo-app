// メモのデータを保存する
import { writable } from "svelte/store";

export const memoData = writable({ title: "", body: "", references: ""});
