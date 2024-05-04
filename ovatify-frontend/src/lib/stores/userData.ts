import type { UserData } from "$lib/types";
import { writable } from "svelte/store";

const initialUserDataState: UserData = {
	id: null,
	token: null,
	name: "",
	img_url: "",
	preferences: {
		data_processing: false,
		data_sharing: false
	}
};

export const userData = writable(initialUserDataState);

export function resetUserData() {
	userData.set(initialUserDataState);
}
