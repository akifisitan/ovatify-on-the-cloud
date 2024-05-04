<script lang="ts">
	import { Input } from "$lib/components/ui/input";
	import { Button } from "$lib/components/ui/button";
	import { Label } from "$lib/components/ui/label";
	import { displayToast } from "$lib/utils/toast";
	import { goto } from "$app/navigation";
	import { Icons } from "$lib/icons";
	import { createUser } from "$lib/services/authService";
	import { fade } from "svelte/transition";
	import { page } from "$app/stores";

	let email = "";
	let password = "";
	let username = "";
	let passwordConfirm = "";
	let loading = false;

	function validateEmail() {
		email = email.trim();
		let error = "";
		if (email.length === 0 || !email.includes("@"))
			error = "Please provide a valid email";
		return error;
	}

	function validateUsername() {
		username = username.trim();
		let error = "";
		if (username.length < 6 || username.length > 16) error = "Please provide a username";
		return error;
	}

	function validatePassword() {
		password = password.trim();
		let error = "";
		if (password.length < 8 || password.length > 16)
			error = "Password must be between 8 and 16 characters long";
		else if (!password.match(/[a-z]/g))
			error = "Password must contain at least one lowercase letter";
		else if (!password.match(/[A-Z]/g))
			error = "Password must contain at least one uppercase letter";
		else if (!password.match(/[0-9]/g))
			error = "Password must contain at least one number";
		else if (!password.match(/[\.\-,\;]/g))
			error = "Password must contain at least one of the following symbols (. , - or ;)";
		return error;
	}

	async function handleSignup() {
		if (loading) return;
		if (password !== passwordConfirm) {
			displayToast({ type: "error", message: "Passwords do not match" });
			return;
		}
		const emailError = validateEmail();
		if (emailError !== "") {
			displayToast({ type: "error", message: emailError });
			return;
		}
		const usernameError = validateUsername();
		if (usernameError !== "") {
			displayToast({ type: "error", message: usernameError });
			return;
		}
		const passwordError = validatePassword();
		if (passwordError !== "") {
			displayToast({ type: "error", message: passwordError });
			return;
		}
		loading = true;
		const response = await createUser({ email, username, password });
		if (response.status !== 201) {
			displayToast({ type: "error", message: "Error signing up" });
			loading = false;
			return;
		}
		displayToast({ type: "success", message: "Account created successfully" });
		const redirectTo = $page.url.searchParams.get("redirect");
		if (redirectTo) {
			goto(`/login?redirect=${redirectTo}`, { replaceState: true });
		} else {
			goto("/login", { replaceState: true });
		}
	}
</script>

<div class="flex flex-col justify-center items-center min-h-[85vh] sm:min-h-screen">
	<div in:fade|global class="flex flex-col justify-center items-center">
		<div class="py-4">
			<Icons.logoWithText />
		</div>
		<div
			class="flex border-[2px] bg-[#1D1F26] text-[#B3BBD8] rounded-2xl justify-center items-center
					 w-[20rem] xsm:w-[24rem] sm:w-[26rem] max-w-[95vw] pb-4 mt-4 mb-8"
		>
			<form
				class="flex flex-col p-4 gap-4 xsm:w-[24rem]"
				on:submit|preventDefault={handleSignup}
			>
				<h1 class="pt-4 text-center text-2xl font-bold">Sign Up</h1>
				<div class="text-[#B3BBD8] placeholder-slate-800">
					<Label for="email">Email</Label>
					<Input
						class="bg-black mt-1"
						type="email"
						placeholder="Enter your email"
						name="email"
						id="email"
						bind:value={email}
					/>
				</div>
				<div class="text-[#B3BBD8] placeholder-slate-800">
					<Label for="username">Username</Label>
					<Input
						class="bg-black mt-1"
						type="text"
						placeholder="Enter your username"
						name="username"
						id="username"
						bind:value={username}
					/>
				</div>
				<div>
					<Label for="password">Password</Label>
					<Input
						class="bg-black mt-1"
						type="password"
						placeholder="Enter your password"
						bind:value={password}
					/>
				</div>
				<div>
					<Label for="confirm-password">Confirm Password</Label>
					<Input
						class="bg-black mt-1"
						type="password"
						name="confirm-password"
						id="confirm-password"
						placeholder="Confirm Password"
						bind:value={passwordConfirm}
					/>
				</div>
				<Button
					variant={!loading ? "outline" : "secondary"}
					type="submit"
					class="font-semibold">{!loading ? "Sign Up" : "Signing up..."}</Button
				>
				<div>
					{#if loading}
						<p class="px-2 text-center sm:px-4 sm:text-start">
							Already have an account? <span class="font-semibold underline">Log In</span>
						</p>
					{:else}
						<p class="px-2 text-center sm:px-4 sm:text-start">
							Already have an account? <a
								href="/login"
								class="transition font-semibold underline hover:text-zinc-300">Log In</a
							>
						</p>
					{/if}
				</div>
			</form>
		</div>
	</div>
</div>
