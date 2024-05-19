import { browser } from "$app/environment";
import { getUserProfile } from "$lib/services/userService";
import { userData } from "$lib/stores/userData";

export const ssr = false;
export const prerender = true;
export const trailingSlash = "always";

export async function load() {
	if (!browser) return;
	const token = localStorage.getItem("accessToken");
	if (!token) return;
	const response = await getUserProfile(token);
	if (response.status === 200) {
		userData.set({ token, ...response.data });
	} else {
		localStorage.removeItem("accessToken");
	}
}
