class ApiConfig {
  // Definido em tempo de build via --dart-define=BASE_URL=...
  // Ex.: flutter build apk --dart-define=BASE_URL=https://doanet.onrender.com
  // Padrão aponta para o backend local (10.0.2.2 = localhost no emulador Android).
  static const String baseUrl = String.fromEnvironment(
    'BASE_URL',
    defaultValue: 'http://10.0.2.2:8000',
  );

  // Timeout generoso para tolerar o "cold start" do Render free tier, que
  // pode levar ~45s para acordar o container na primeira requisição.
  static const Duration requestTimeout = Duration(seconds: 60);
}
