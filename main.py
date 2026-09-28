import os
import sys
import time


USE_COLOR = sys.stdout.isatty()


def color(text, code):
	if USE_COLOR:
		return f"\033[{code}m{text}\033[0m"
	return text


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


def type_text(text, delay=0.01):
	for character in text:
		print(character, end="", flush=True)
		time.sleep(delay)
	print()


def divider():
	print(color("═" * 64, "36"))


def show_title():
	clear_screen()
	print(color(r"""
GALAXY EXPLORERS!!!:	
				 SIGNALS OF THE LOST MOON
""", "35"))
	divider()
	print(color("         [ ENTER ]  BAŞLAMAK İÇİN BİR TUŞA BAS", "33"))
	divider()
	input()


def choose(prompt, choices):
	while True:
		print()
		type_text(prompt)
		for key, label in choices.items():
			print(color(f"  [{key}]", "33"), label)
		answer = input(color("\n> ", "32")).strip().lower()
		if answer in choices:
			return answer
		print(color("Geçersiz seçim. Konsol seni duymadı...", "31"))


def ending(title, message):
	print()
	divider()
	print(color(f" SON: {title}", "35"))
	divider()
	type_text(message)
	print()
	input(color("Ana menüye dönmek için ENTER...", "33"))


def play():
	show_title()
	clear_screen()
	print(color("YIL 2094 // AYIN KARANLIK YÜZÜ // 03:17", "36"))
	divider()
	type_text("Telsizinden gelen sinyal, yıllardır kayıp olan NOVA-7 kolonisinden.")
	type_text("Geminin yakıtı tek bir inişe yetiyor. Karar zamanı, gezgin.")

	first_choice = choose(
		"Sinyal iki farklı kaynaktan geliyor. Hangisini takip ediyorsun?",
		{"1": "Kırmızı kule: Güçlü ama düzensiz sinyal", "2": "Mavi mağara: Zayıf ama düzenli sinyal"},
	)

	clear_screen()
	if first_choice == "1":
		type_text("Kırmızı kuleye indin. Paslı kapının ardında eski bir bakım robotu çalışıyor.")
		type_text("Robot sana bir enerji hücresi uzatıyor, fakat karşılığında çekirdeğini istiyor.")
		second_choice = choose(
			"Ne yapacaksın?",
			{"1": "Enerji hücresini al ve robotu kapat", "2": "Robotu onar ve hücreyi paylaş"},
		)
		if second_choice == "1":
			ending(
				"KULELERİN KRALI",
				"Güç hücresi gemini çalıştırdı. Koloniyi geride bıraktın, ama kuledeki\n"
				"kırmızı ışık hâlâ seni izliyor. Bazen hayatta kalmak, doğru seçim değildir.",
			)
		else:
			ending(
				"YENİ ORTAKLIK",
				"Robot seni koloninin yeraltı kapılarına götürdü. Birlikte NOVA-7'yi yeniden\n"
				"uyandırdınız. Gezegen artık yalnız değil.",
			)
	else:
		type_text("Mavi mağara seni kristallerle dolu bir salona götürdü.")
		type_text("Kristaller, zihninde üç kelime yankılatıyor: 'Sinyali geri gönder.'")
		second_choice = choose(
			"Mesajı nereye göndereceksin?",
			{"1": "Dünyaya: Yardım çağrısı", "2": "Uzaya: Bilinmeyenlere cevap"},
		)
		if second_choice == "1":
			ending(
				"EVE DÖNÜŞ",
				"Dünya sinyalini aldı. Kurtarma filosu yolda. Sen, karanlıkta beklerken\n"
				"ilk kez gökyüzünü güvenli hissettin.",
			)
		else:
			ending(
				"YILDIZLARIN ÖTESİ",
				"Sinyal boşluğa karıştı. Cevap anında geldi: NOVA-7'den değil, başka bir\n"
				"galaksiden. Motorlarını çalıştırdın. Macera şimdi gerçekten başlıyor.",
			)


def main():
	try:
		play()
	except KeyboardInterrupt:
		print("\n\nOyun kapatıldı. Sinyal kesildi.")


if __name__ == "__main__":
	main()