<script lang="ts">
	import { goto } from "$app/navigation";
	import SideNav from "./SideNav.svelte";
	import TopNav from "./TopNav.svelte";
	import { page } from "$app/stores";
	import { userData } from "$lib/stores/userData";

	$: if (!$userData.token) {
		const origin = $page.url.pathname;
		if (origin === "/") {
			goto("/login", { replaceState: true });
		} else {
			goto(`/login?redirect=${origin}`, { replaceState: true });
		}
	}
</script>

{#if $userData.token}
	<main>
		<TopNav />
		<div class="flex">
			<SideNav />
			<!-- Page Content -->
			<div class="p-4 w-full">
				<slot />
			</div>
		</div>
	</main>
{/if}
