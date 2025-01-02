function populateData() {
    document.getElementById('parameterinput').innerHTML = `
        <div class="text-gray-600">Age: <span class="text-gray-900">40</span></div>
        <div class="text-gray-600">Sex: <span class="text-gray-900">M</span></div>
        <div class="text-gray-600">Chest Pain Type: <span class="text-gray-900">ATA</span></div>
        <div class="text-gray-600">Resting Blood Pressure: <span class="text-gray-900">140 mm Hg</span></div>
        <div class="text-gray-600">Cholesterol: <span class="text-gray-900">289 mg/dl</span></div>
        <div class="text-gray-600">Fasting Blood Sugar: <span class="text-gray-900">0</span></div>
        <div class="text-gray-600">Resting ECG: <span class="text-gray-900">Normal</span></div>
        <div class="text-gray-600">Maximum Heart Rate: <span class="text-gray-900">172 bpm</span></div>
        <div class="text-gray-600">Exercise-Induced Angina: <span class="text-gray-900">N</span></div>
        <div class="text-gray-600">Oldpeak (ST Depression): <span class="text-gray-900">0</span></div>
        <div class="text-gray-600">ST Slope: <span class="text-gray-900">Up</span></div>
    `;

    document.getElementById('hasilPrediksi').innerHTML = `
        <span class="font-semibold">Prediction:</span> 
        <span class="text-red-600">Normal</span>
    `;

    document.getElementById('summarysaja').innerHTML = `
        <div class="text-gray-800">Alhamdulillah! Berdasarkan data kesehatan yang diberikan, Kamu termasuk dalam kategori \"Normal\" alias tidak dalam risiko penyakit jantung saat ini. 🎉\n\nNamun, ada beberapa hal yang perlu kita perhatikan nih agar tetap bugar dan sehat:\n\n1. Tekanan Darah: Tekanan darah kamu sedikit tinggi di angka 140 mm Hg. Mungkin ada baiknya mengurangi asupan garam, lebih sering berolahraga, atau sekadar relaksasi. Ingat, puncak prestasi kesehatan dimulai dari tekanan darah yang oke.\n   \n2. Kolesterol: Kolesterol kamu juga cukup tinggi di 289 mg/dl. Yuk, coba lebih banyak makan makanan yang rendah lemak jenuh, seperti ikan, sayuran hijau, dan kacang-kacangan. Jika perlu, konsultasikan ke dokter untuk intervensi medis lebih lanjut.\n\n3. Gaya Hidup: Kamu masih muda, 40 tahun adalah masa-masa produktif nih. Yuk, rutin olahraga minimal 30 menit sehari, 5 kali seminggu. Jangan lupa juga untuk berhenti merokok jika kamu merokok dan kurangi konsumsi alkohol.\n\n4. Diet Sehat: Makan lebih banyak sayuran, buah-buahan, dan biji-bijian. Hindari makanan cepat saji yang kurang baik untuk kesehatan.\n\n5. Rutin periksa kesehatan: Tetaplah melakukan pemeriksaan kesehatan secara rutin. Kajian detil dan berkala akan membantu mencegah atau mengenali masalah lebih awal.\n\nJangan lupa istirahat yang cukup dan kelola stres dengan baik ya. Karena kalau kita sehat, hidup jadi lebih mudah dan bahagia. 😉 \n\nOke, sampai sini dulu ya. Sehat terus dan tetap semangat! Oh iya, ada pantun nih buat kamu:\n\n\"Pergi ke hutan mencari petai,\nKolesterol turun hati pun damai.\"\n\nJaga kesehatan ya, bro! Semangat! 💪😊<div>
    `;
}

function populate(event) {
    event.preventDefault();
    populateData();
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('predictButton').addEventListener('click', populate);
});
