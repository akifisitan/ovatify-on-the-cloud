import { resetUserData } from "$lib/stores/userData";
import * as api from "$lib/utils/api";

export async function createUser(body: {
	email: string;
	username: string;
	password: string;
}) {
	const response = await api.post("users/create-user/", null, body);
	return response;
}

export async function login(email: string, password: string) {
	const response = await api.post("users/login/", null, { email, password });
	return response;
}

export async function verifyToken(token: string) {
	console.log("verifying token", token);
	// const response = await api.post("users/verify-token/", token);
	return { status: 200, data: { refresh: token, access: "" }, error: null };
}

export function signOut() {
	localStorage.removeItem("accessToken");
	resetUserData();
}
