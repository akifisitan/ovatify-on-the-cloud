<script lang="ts">
	import { goto } from "$app/navigation";
	import { userData } from "$lib/stores/userData";
	import { page } from "$app/stores";
	import { isValidRoute } from "$lib/utils/validation";
	import { verifyToken } from "$lib/services/authService";

	$: handleRedirect();

	async function handleRedirect() {
		if (!$userData.token) return;
		const response = await verifyToken($userData.token);
		if (response.status !== 200) return;
		const redirectTo = $page.url.searchParams.get("redirect");
		if (redirectTo && isValidRoute(redirectTo)) {
			goto(redirectTo, { replaceState: true });
		} else {
			goto("/", { replaceState: true });
		}
	}
</script>

<slot />
