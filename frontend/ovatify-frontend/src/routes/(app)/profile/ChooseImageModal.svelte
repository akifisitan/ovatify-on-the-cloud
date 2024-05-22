<script lang="ts">
	import { buttonVariants } from "$lib/components/ui/button";
	import * as Dialog from "$lib/components/ui/dialog";
	import { userData } from "$lib/stores/userData";
	import { cn } from "$lib/utils";
	import { avatars } from "$lib/utils/avatars";
	import { displayToast } from "$lib/utils/toast";
	import { Pencil } from "lucide-svelte";
	import { createEventDispatcher } from "svelte";
	import { Button } from "$lib/components/ui/button";
	import { editUserImage } from "$lib/services/userService";
	import * as Avatar from "$lib/components/ui/avatar";

	let dialogOpen = false;

	const dispatch = createEventDispatcher();

	let image: File | null = null;
	let loading = false;

	function setImage(event: Event) {
		const target = event.target as HTMLInputElement;
		image = target?.files?.[0] ?? null;
	}

	function validateFile() {
		if (!image) {
			displayToast({ type: "error", message: "No image selected" });
			return false;
		}
		const fileSplit = image.name.split(".");
		const fileExtension = fileSplit[fileSplit.length - 1].toLowerCase();
		if (
			fileExtension !== "png" &&
			fileExtension !== "jpg" &&
			fileExtension !== "jpeg" &&
			fileExtension !== "webp"
		) {
			displayToast({ type: "error", message: "The file must be an image" });
			return false;
		}
		return true;
	}

	async function modifyImage() {
		if (loading) return;
		if (!validateFile()) return;
		loading = true;
		const token = $userData.token!;
		const response = await editUserImage(token, image!);
		console.log(response);
		if (response.status === 201) {
			displayToast({ type: "success", message: "Image updated successfully" });
		} else if (response.status === 400) {
			displayToast({
				type: "error",
				message: "Please make sure the image is appropriate"
			});
		} else {
			displayToast({ type: "error", message: "Error updating image" });
		}
		dispatch("selectImage", URL.createObjectURL(image!));
		dialogOpen = false;
		loading = false;
		image = null;
	}
</script>

<Dialog.Root bind:open={dialogOpen}>
	<Dialog.Trigger
		class="absolute top-0 right-0 rounded-full bg-slate-950 p-1 hover:bg-slate-800"
		><Pencil class="h-5 w-5" /></Dialog.Trigger
	>
	<Dialog.Content
		class="flex justify-center rounded-lg px-2 xsm:px-6 w-3/4 md:max-w-[70vw] lg:max-w-[36rem] pt-10 min-h-[24rem]"
	>
		<div class="w-full">
			<div class="py-2">
				<h1 class="text-2xl font-semibold text-center">Choose a new image</h1>
			</div>
			<form
				enctype="multipart/form-data"
				class="flex flex-col gap-4 min-h-[24rem] justify-center items-center"
			>
				<Avatar.Root class="w-32 h-32 text-3xl">
					<Avatar.Image
						src={image ? URL.createObjectURL(image) : $userData.img_url}
						alt={image ? image.name : "None"}
					/>
					<Avatar.Fallback>None</Avatar.Fallback>
				</Avatar.Root>
				{#if !image}
					<label
						for="image-upload"
						class={cn(
							buttonVariants({ variant: "outline" }),
							"w-4/5 py-8 cursor-pointer"
						)}>Choose Image</label
					>
					<input
						id="image-upload"
						type="file"
						accept=".jpg, .jpeg, .png .webp"
						class="hidden"
						on:change={setImage}
						disabled={loading}
					/>
				{:else}
					<div class="flex flex-col gap-2 items-center justify-center w-full">
						<Button
							on:click={modifyImage}
							variant="outline"
							class={cn("w-4/5", {
								"text-black bg-indigo-300 hover:bg-indigo-200 hover:text-black": !loading,
								"bg-secondary hover:bg-secondary opacity-50 cursor-not-allowed": loading
							})}>{loading ? "Uploading..." : "Upload Image"}</Button
						>
						<Button
							on:click={() => {
								if (!loading) {
									image = null;
								}
							}}
							variant="outline"
							class={cn("w-4/5", {
								"text-black bg-red-500 hover:bg-red-400 hover:text-black": !loading,
								"bg-secondary hover:bg-secondary opacity-50 cursor-not-allowed": loading
							})}>Remove Image</Button
						>
					</div>
				{/if}
			</form>
		</div>
	</Dialog.Content>
</Dialog.Root>

<style lang="postcss">
	.avatars {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(4rem, 1fr));
	}
</style>
