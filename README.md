# Healthcare Auth (Django)

Small Django project that demonstrates user signup/login with an extended user profile and a Tailwind-based UI.

Contents

- `manage.py` — Django management script
- `Auth/settings.py` — project settings (uses python-decouple for secrets)
- `core/` — main app: models, forms, views, templates for signup/login/dashboard
- `theme/` — Tailwind app (contains `static_src` with `package.json`)
- `db.sqlite3` — default SQLite database (included)

Quick start

1. Create a Python virtual environment and activate it:

   Windows (PowerShell):

   ```powershell
   python -m venv .venv; .\.venv\Scripts\Activate.ps1
   ```

2. Install Python dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create (or update) `.env` with required environment variables. At minimum set:

   ```text
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

4. Run migrations (creates necessary tables):

   ```powershell
   python manage.py migrate
   ```

5. (Optional) Create a superuser for the admin site:

   ```powershell
   python manage.py createsuperuser
   ```

6. Tailwind / frontend build

   This project uses `django-tailwind` and a `theme/static_src/package.json`.

   - Install node dependencies (from the `theme/static_src` directory):

   ```powershell
   cd theme\static_src; npm install
   ```

   - For development (watch + rebuild CSS):

   ```powershell
   npm run dev
   ```

   - To build production CSS:

   ```powershell
   npm run build
   ```

   Note: `NPM_BIN_PATH` is set in `settings.py` to a common Windows path for npm. Adjust if your npm location differs.

7. Run the development server

   ```powershell
   python manage.py runserver
   ```

   Or use the Procfile-style commands in `Procfile.tailwind` (use with `honcho` or similar):

   ```powershell
   honcho start -f Procfile.tailwind
   ```

Project highlights

- A `UserProfile` model extends Django's `User` via one-to-one relation (`core/models.py`).
- `core/forms.py` contains a `SignUpForm` (extends `UserCreationForm`) and `CustomLoginForm`.
- Views live in `core/views.py`: `signup_view`, `login_view`, `logout_view`, `dashboard_view`.
- Templates use Tailwind utility classes and are in `core/templates/`.
- Static/Tailwind configuration lives in the `theme` app; the Tailwind build outputs to `theme/../static/css/dist/styles.css` as configured in `package.json`.

Notes and troubleshooting

- Database: This project uses `db.sqlite3` by default. If you plan to reset or remove it, re-run `migrate` and recreate any users.
- Media: Uploaded profile images are stored in `media/` (see `MEDIA_ROOT` in settings).
- If `SECRET_KEY` or other env vars are missing, the app will raise an error on startup (settings uses `python-decouple`).
- If Tailwind styles do not update, ensure `npm run dev` is running and the `@source` paths in `theme/static_src/src/styles.css` include your templates.

Development checklist

- [ ] Activate virtualenv
- [ ] Install Python deps
- [ ] Install Node deps inside `theme/static_src`
- [ ] Run migrations
- [ ] Run Tailwind dev or build
- [ ] Start Django server

License

This project contains example code and UI for learning purposes.
