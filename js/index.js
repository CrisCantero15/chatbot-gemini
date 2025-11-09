document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const input = document.querySelector("input")
    const conversationBox = document.querySelector(".conversation")
    const boxLoading = document.querySelector(".boxLoading")

    form.addEventListener("submit", async (e) => {

        e.preventDefault()
        
        const inputMessage = input.value.trim()
        input.value = ""
        if (!inputMessage) return

        const payload = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt: inputMessage })
        }

        boxLoading.style.display = "block"

        try {

            const response = await fetch("/api/chat", payload)
            const data = await response.json()    
            
            if (data.message) {
                const newMessage = `
                    <h2>Usuario:</h2>
                    <p>${inputMessage}</p>
                    <h2>Chatbot:</h2>
                    <p>${data.message}</p>
                `
                conversationBox.innerHTML += newMessage
                boxLoading.style.display = "none"
                return
            }

            if (data.error) {
                const newMessage = `
                    <h2>Usuario:</h2>
                    <p>${inputMessage}</p>
                    <h2>Chatbot:</h2>
                    <p>${data.error}</p>
                `
                conversationBox.innerHTML += newMessage
                boxLoading.style.display = "none"
                return
            }

            const newMessage = `
                <h2>Usuario:</h2>
                <p>${inputMessage}</p>
                <h2>Chatbot:</h2>
                <p>No se pudo generar una respuesta</p>
            `
            conversationBox.innerHTML += newMessage
            boxLoading.style.display = "none"
            return

        } catch (error) {
            
            const newMessage = `
                <h2>Usuario:</h2>
                <p>${inputMessage}</p>
                <h2>Chatbot:</h2>
                <p>Error al procesar la solicitud: ${error}</p>
            `
            conversationBox.innerHTML += newMessage
            boxLoading.style.display = "none"
            return

        }

    })

})