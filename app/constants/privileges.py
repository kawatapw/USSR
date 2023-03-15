from __future__ import annotations

from enum import IntFlag


class Privileges(IntFlag):
    """Bitwise enumerations for Ripple privileges."""
    NoPrivs             = 0        # not previously defined.
    PublicUser          = 1        # USER_PUBLIC
    NormalUser          = 2 << 0   # USER_NORMAL
    Donor               = 2 << 1   # USER_DONOR
    AccessRAP           = 2 << 2   # ADMIN_ACCESS_RAP
    ManageUsers         = 2 << 3   # ADMIN_MANAGE_USERS
    BanUsers            = 2 << 4   # ADMIN_BAN_USERS
    SilenceUsers        = 2 << 5   # ADMIN_SILENCE_USERS
    WipeUsers           = 2 << 6   # ADMIN_WIPE_USERS
    ManageBeatmaps      = 2 << 7   # ADMIN_MANAGE_BEATMAPS
    ManageServers       = 2 << 8   # ADMIN_MANAGE_SERVERS
    ManageSettings      = 2 << 9   # ADMIN_MANAGE_SETTINGS 
    ManageBetaKeys      = 2 << 10  # ADMIN_BETAKEYS
    ManageReports       = 2 << 11  # ADMIN_MANAGE_REPORTS
    ManageDocs          = 2 << 12  # ADMIN_MANAGE_DOCS
    ManageBadges        = 2 << 13  # ADMIN_MANAGE_BADGES
    ViewRAPLog          = 2 << 14  # ADMIN_VIEW_RAP_LOGS
    ManagePrivs         = 2 << 15  # ADMIN_MANAGE_PRIVILEGES
    SendAlerts          = 2 << 16  # ADMIN_SEND_ALERTS
    ChatMod             = 2 << 17  # ADMIN_CHAT_MOD
    KickUsers           = 2 << 18  # ADMIN_KICK_USERS
    PendingVerify       = 2 << 19  # USER_PENDING_VERIFICATION
    TournamentStaff     = 2 << 20  # USER_TOURNAMENT_STAFF
    Caker               = 2 << 21  # ADMIN_CAKER
    ManageClans         = 2 << 27  # PANEL_MANAGE_CLANS
    ViewIps             = 2 << 28  # PANEL_VIEW_IPS
    IsBot               = 2 << 30  # BOT_USER
    # Realistik Panel Exclusive Permissions. not previously defined, not all are used.
    ViewTopScores       = 2 << 31  
    PanelNominate       = 2 << 32
    PanelNominateAccept = 2 << 33
    PanelOverwatch      = 2 << 34
    PanelErrorLogs      = 2 << 35


    @property
    def is_restricted(self) -> bool:
        """Checks if user is restricted."""
        return (
            (self & Privileges.NormalUser) and not (self & Privileges.PublicUser)
        ) or self.is_banned

    @property
    def is_banned(self) -> bool:
        """Checks if user is banned."""
        return self & Privileges.NormalUser == 0

    def has_privilege(self, priv: Privileges) -> bool:
        """Returns a bool corresponding to whether the privilege flag contains
        a single privilege.
        Note:
            This is a check for a **singular** privilege. If you include
                multiple, just the presence of one would result in
                `True` being returned.
        """

        return self & priv != 0
