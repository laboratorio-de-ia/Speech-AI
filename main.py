"""
====================================================
 Speech AI - Main
----------------------------------------------------
Sprint 6.3

Ponto de entrada da aplicação.

Responsável apenas por iniciar a aplicação.

Toda a orquestração fica em SpeechAIApp.
====================================================
"""

from app import SpeechAIApp


def main():

    app = SpeechAIApp()

    app.run()


if __name__ == "__main__":
    main()