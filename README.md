# Git Class Lab

A deliberately messy repository. Things will break. That is the point.

## Ground rules

- Read the error before you ask. Git's error messages are unusually good.
- Work in pairs. The person with less Git experience types.
- Nothing here is precious. If you tangle your copy beyond repair, delete the
  folder and clone it again.

## The four phases

1. **You cannot push.** Add a file about yourself to `students/`, commit it,
   and try to push. Discover what write access means.
2. **Two people, one branch.** Two of you get access, both change `port:` in
   `config/settings.yml`, and get in each other's way.
3. **Branches.** Work in parallel on the same line of the same file without
   colliding. Open a pull request. Watch `main` move underneath you.
4. **Forks.** Fork this repository, push to your own copy, and open a pull
   request asking me to take your change.

## The commands from today

| Command | What it does |
|---|---|
| `git clone URL` | Take a full copy of a project |
| `git status` | What have I changed? Where am I? |
| `git add FILE` | Mark a change to go in the next save |
| `git commit -m "..."` | Save a snapshot. Local. No network. |
| `git log --oneline` | The story so far |
| `git push` | Send commits to a server someone else owns |
| `git pull` | Fetch other people's work and merge it in |
| `git switch -c NAME` | Start a branch and move onto it |
| `git switch NAME` | Move to an existing branch |
| `git merge NAME` | Bring another branch into this one |
| `git merge --abort` | Undo a merge that went sideways |

## Errors you will meet, and what they mean

**`Permission to OWNER/REPO.git denied to YOU` (403)**
You are not allowed to write here. Someone has to give you access, or you fork.

**`! [rejected] main -> main (fetch first)`**
You are allowed to write, but your history and the server's have split apart.
Run `git pull` to bring their work in, then push again.

**`CONFLICT (content): Merge conflict in FILE`**
Two people changed the same line. Git merged everything else and stopped here
because only a human can decide. Edit the file, delete the `<<<<<<<`,
`=======` and `>>>>>>>` markers, then `git add` and `git commit`.

**`This branch has conflicts that must be resolved`** (on a pull request)
`main` changed while you were working. Merge `main` into your branch, resolve,
and push again.