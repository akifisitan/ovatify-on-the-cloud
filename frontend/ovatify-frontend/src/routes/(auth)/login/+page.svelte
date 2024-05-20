<script lang="ts">
	import { Input } from "$lib/components/ui/input";
	import { Button } from "$lib/components/ui/button";
	import { Label } from "$lib/components/ui/label";
	import { displayToast } from "$lib/utils/toast";
	import { Icons } from "$lib/icons";
	import { login } from "$lib/services/authService";
	import { getUserProfile } from "$lib/services/userService";
	import { userData } from "$lib/stores/userData";
	import { goto } from "$app/navigation";
	import { fade } from "svelte/transition";
	import { page } from "$app/stores";

	let email = "";
	let password = "";
	let loading = false;

	function validateEmail() {
		email = email.trim();
		let error = "";
		if (email.length === 0 || !email.includes("@"))
			error = "Please provide a valid email";
		return error;
	}

	function validatePassword() {
		password = password.trim();
		let error = "";
		if (password.length < 8 || password.length > 16)
			error = "Password must be between 8 and 16 characters long";
		return error;
	}

	async function handleLogin() {
		if (loading) return;
		const emailError = validateEmail();
		if (emailError !== "") {
			displayToast({ type: "error", message: emailError });
			return;
		}
		const passwordError = validatePassword();
		if (passwordError !== "") {
			displayToast({ type: "error", message: passwordError });
			return;
		}
		loading = true;
		const response = await login(email, password);
		if (response.status !== 200) {
			displayToast({ type: "error", message: "Error logging in" });
			loading = false;
			return;
		}
		const token = response.data.access;
		localStorage.setItem("accessToken", token);
		const getUserProfileResponse = await getUserProfile(token);
		userData.set({ token, ...getUserProfileResponse.data });
		const redirectTo = $page.url.searchParams.get("redirect");
		if (redirectTo) {
			goto(redirectTo, { replaceState: true });
		} else {
			goto("/", { replaceState: true });
		}
	}
</script>

<div class="flex flex-col justify-center items-center min-h-[85vh] sm:min-h-screen">
	<div in:fade|global class="flex flex-col justify-center items-center">
		<div class="py-4">
			<Icons.logoWithText />
		</div>
		<div
			class="flex border-2 bg-[#1D1F26] text-[#B3BBD8] rounded-2xl justify-center items-center
					 w-[20rem] xsm:w-[24rem] sm:w-[26rem] max-w-[90vw] pb-4 mt-4 mb-8"
		>
			<form
				class="flex flex-col p-4 gap-4 xsm:w-[24rem]"
				on:submit|preventDefault={handleLogin}
			>
				<h1 class="pt-4 text-center text-2xl font-bold">Log In</h1>
				<div class="text-[#B3BBD8] placeholder-slate-800">
					<Label for="email">Email</Label>
					<Input
						class="bg-black mt-1"
						type="email"
						id="email"
						name="email"
						tabindex={1}
						placeholder="Enter your email"
						bind:value={email}
					/>
				</div>
				<div>
					<div class="flex justify-between items-center font-medium text-sm">
						<Label for="password">Password</Label>
						{#if loading}
							<p class="select-none">Forgot password?</p>
						{:else}
							<a href="/reset-password" class="transition hover:opacity-75" tabindex={4}
								>Forgot password?</a
							>
						{/if}
					</div>
					<Input
						class="bg-black mt-1"
						type="password"
						id="password"
						name="password"
						tabindex={2}
						placeholder="Enter your password"
						bind:value={password}
					/>
				</div>
				<Button
					variant={!loading ? "outline" : "secondary"}
					type="submit"
					tabindex={3}
					class="font-semibold">{!loading ? "Log In" : "Logging in..."}</Button
				>
				<div>
					{#if loading}
						<p class="px-2 text-center sm:px-4 sm:text-start">
							Don't have an account? <span class="font-semibold underline">Sign up</span>
						</p>
					{:else}
						<p class="px-2 text-center sm:px-4 sm:text-start">
							Don't have an account? <a
								href="/signup"
								class="transition font-semibold underline hover:text-zinc-300">Sign up</a
							>
						</p>
					{/if}
				</div>
			</form>
		</div>
	</div>
</div>
