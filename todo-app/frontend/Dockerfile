# ベースイメージとしてNode.jsを使用
FROM node:16

# 作業ディレクトリを設定
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピーし、依存関係をインストール
COPY package*.json ./
RUN npm install

# ソースコードをコピー
COPY . .

# ビルド
RUN npm run build

# Nginxを使って静的ファイルを提供する
FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html

# Nginxを起動
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
