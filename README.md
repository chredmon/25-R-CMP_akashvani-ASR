# 25-R-CMP_akashvani-ASR
Testing several recent ASR systems against multilingual regional news broadcasts from All India Radio

## Languages and stations tested

| No. | Language      | Station            | Duration (h:m) | Total (per lg) |
| :--- | :------------ | :----------------- | :-------------- | :-------------- |
| 1   | Assamese      | Dibrugarh          | 1:22           | 2:43           |
|     |               | Guwahati           | 1:20           |                |
| 2   | Bengali       | Agartala           | 1:20           | 5:58           |
|     |               | Kolkata            | 2:44           |                |
|     |               | Silchar            | 1:55           |                |
| 3   | Bhojpuri      | Gorakhpur          | 1:20           | 1:20           |
| 4   | Bhutia        | Gangtok            | 1:16           | 1:16           |
| 5   | Chhattisgarhi | Raipur             | 2:27           | 2:27           |
| 6   | Dogri         | Jammu              | 2:32           | 2:32           |
| 7   | English       | Itanagar           | 1:20           | 4:14           |
|     |               | Kohima             | 1:28           |                |
|     |               | Shillong           | 1:25           |                |
| 8   | Gojri         | Jammu              | 1:24           | 1:24           |
| 9   | Gujarati      | Ahmedabad          | 2:35           | 3:50           |
|     |               | Bhuj               | 1:15           |                |
| 10  | Hindi         | Bhopal             | 2:23           | 26:05          |
|     |               | Chandigarh         | 1:15           |                |
|     |               | Dehradun           | 2:42           |                |
|     |               | Gorakhpur          | 2:40           |                |
|     |               | Itanagar           | 1:19           |                |
|     |               | Jaipur             | 2:39           |                |
|     |               | Lucknow            | 2:41           |                |
|     |               | Patna              | 3:39           |                |
|     |               | Raipur             | 2:49           |                |
|     |               | Ranchi             | 2:43           |                |
|     |               | Shimla             | 1:15           |                |
| 11  | Kannada       | Bengaluru          | 2:37           | 5:20           |
|     |               | Dharwad            | 2:42           |                |
| 12  | Konkani       | Panaji             | 1:23           | 1:23           |
| 13  | Lepcha        | Gangtok            | 1:10           | 1:10           |
| 14  | Maithili      | Patna              | 1:24           | 1:24           |
| 15  | Malayalam     | Calicut            | 2:37           | 5:19           |
|     |               | Thiruvananthapuram | 2:42           |                |
| 16  | Manipuri      | Imphal             | 2:34           | 2:34           |
| 17  | Marathi       | C S Nagar          | 2:40           | 10:34          |
|     |               | Mumbai             | 2:36           |                |
|     |               | Nagpur             | 2:37           |                |
|     |               | Pune               | 2:41           |                |
| 18  | Mizo          | Aizawl             | 2:57           | 2:57           |
| 19  | Nepali        | Gangtok            | 1:21           | 4:03           |
|     |               | Kurseong           | 2:42           |                |
| 20  | Odia          | Cuttack            | 1:23           | 1:23           |
| 21  | Punjabi       | Jalandhar          | 1:24           | 1:24           |
| 22  | Rajasthani    | Jaipur             | 3:17           | 3:17           |
| 23  | Sambalpuri    | Sambalpur          | 1:21           | 1:21           |
| 24  | Tamil         | Chennai            | 2:39           | 8:03           |
|     |               | Pudducherry        | 2:40           |                |
|     |               | Tiruchirapalli     | 2:44           |                |
| 25  | Telugu        | Hyderabad          | 2:33           | 7:40           |
|     |               | Vijayawada         | 2:32           |                |
|     |               | Visakhapatnam      | 2:34           |                |
| 26  | Urdu          | C S Nagar          | 2:37           | 6:28           |
|     |               | Hyderabad          | 2:31           |                |
|     |               | Srinagar           | 1:20           |                |


## Models

The following models were tested to cover both some of the most accurate 
multilingual ASR models to date and to cover several of the key interfaces 
to most devices (i.e., Google, Apple, Microsoft, Amazon). Further, AI4Bharat's 
Conformer model is used as a benchmark for comparison which is specialised in 
Indic languages.

- AI4Bharat (IndicConformer)
- OpenAI (GPT-4o-mini, Whisper)
- Elevenlabs (Scribe)
- Google (Chirp)
- Microsoft (Azure)
- Apple
- Amazon


