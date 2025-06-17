"""Minimal WishGalaxy Telegram bot.

This module implements a few command handlers using ``python-telegram-bot``.
Only very small placeholder logic is provided as a starting point for the real
project.
"""

from __future__ import annotations

import logging
import os
from collections import defaultdict
from typing import DefaultDict, Dict

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)


# In-memory storage for user roles. Real applications should persist this.
user_roles: DefaultDict[int, str] = defaultdict(lambda: "guest")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message."""
    user_id = update.effective_user.id
    role = user_roles[user_id]
    await update.message.reply_text(
        f"Welcome to WishGalaxy! Your current role is '{role}'."
    )


async def order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Placeholder for the ordering flow."""
    await update.message.reply_text("Ordering is not implemented yet.")


async def me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Display basic user info."""
    user_id = update.effective_user.id
    role = user_roles[user_id]
    await update.message.reply_text(f"Your role: {role}")


async def switch_role(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Switch a user's role.

    Usage: /switch_role <role>
    """

    if not context.args:
        await update.message.reply_text("Usage: /switch_role <role>")
        return

    new_role = context.args[0]
    user_id = update.effective_user.id
    user_roles[user_id] = new_role
    await update.message.reply_text(f"Role switched to {new_role}")


async def top(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show a placeholder ranking."""
    await update.message.reply_text("Top list is empty.")


async def shop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show a placeholder shop."""
    await update.message.reply_text("Star coin shop coming soon.")


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show a placeholder profile."""
    await update.message.reply_text("Profile feature is under construction.")


async def salary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show salary information placeholder."""
    await update.message.reply_text("Salary info will be available at month end.")


def main() -> None:
    """Entry point for the Telegram bot."""

    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN environment variable not set")

    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("me", me))
    app.add_handler(CommandHandler("switch_role", switch_role))
    app.add_handler(CommandHandler("top", top))
    app.add_handler(CommandHandler("shop", shop))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("salary", salary))

    app.run_polling()


if __name__ == "__main__":
    main()
