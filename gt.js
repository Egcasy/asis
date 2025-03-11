
document.addEventListener("DOMContentLoaded", function () {
  const shareButtons = document.querySelectorAll(".share-button");

  shareButtons.forEach(button => {
    button.addEventListener("click", function () {
      const shareOptions = document.createElement("div");
      shareOptions.className = "share-options";

      const shareUrl = button.getAttribute("data-url") || window.location.href;
      const shareText = button.getAttribute("data-title") || "Check out this amazing content!";

      const facebookLink = document.createElement("a");
      facebookLink.href = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(shareUrl)}`;
      facebookLink.target = "_blank";
      facebookLink.innerText = "Share on Facebook";

      const twitterLink = document.createElement("a");
      twitterLink.href = `https://twitter.com/intent/tweet?text=${encodeURIComponent(shareText)}&url=${encodeURIComponent(shareUrl)}`;
      twitterLink.target = "_blank";
      twitterLink.innerText = "Share on Twitter";

      const whatsappLink = document.createElement("a");
      whatsappLink.href = `https://api.whatsapp.com/send?text=${encodeURIComponent(shareText)}%20${encodeURIComponent(shareUrl)}`;
      whatsappLink.target = "_blank";
      whatsappLink.innerText = "Share on WhatsApp";

      shareOptions.appendChild(facebookLink);
      shareOptions.appendChild(twitterLink);
      shareOptions.appendChild(whatsappLink);

      document.querySelectorAll(".share-options").forEach(el => el.remove());

      document.body.appendChild(shareOptions);

      const rect = button.getBoundingClientRect();
      shareOptions.style.position = "absolute";
      shareOptions.style.top = `${rect.bottom + window.scrollY}px`;
      shareOptions.style.left = `${rect.left}px`;
      shareOptions.style.display = "block";

      document.addEventListener("click", function hideOptions(event) {
        if (!shareOptions.contains(event.target)) {
          shareOptions.remove();
          document.removeEventListener("click", hideOptions);
        }
      });
    });
  });
});