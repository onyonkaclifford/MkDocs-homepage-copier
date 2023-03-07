import os
import shutil

from mkdocs.config.defaults import MkDocsConfig

from copier import HomepageCopier


def clean_up(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


def test_homepage_copy_true():
    temp_dir = os.path.join("tests", "test_homepage_copy_true")
    src_file = "README.md"
    dest_file = os.path.join(temp_dir, "index.md")
    copier = HomepageCopier()
    config = MkDocsConfig()

    copier.config["copy"] = True
    copier.config["src"] = src_file
    copier.config["dest"] = dest_file
    copier.config["extras"] = []

    clean_up(temp_dir)
    os.makedirs(temp_dir)

    _ = copier.on_config(config)
    assert os.path.exists(dest_file)

    copier.on_post_build(config)
    assert not os.path.exists(dest_file)

    clean_up(temp_dir)


def test_homepage_copy_false():
    temp_dir = os.path.join("tests", "test_homepage_copy_false")
    src_file = "README.md"
    dest_file = os.path.join(temp_dir, "index.md")
    copier = HomepageCopier()
    config = MkDocsConfig()

    copier.config["copy"] = False
    copier.config["src"] = src_file
    copier.config["dest"] = dest_file
    copier.config["extras"] = []

    clean_up(temp_dir)
    os.makedirs(temp_dir)

    _ = copier.on_config(config)
    assert not os.path.exists(dest_file)

    clean_up(temp_dir)


def test_extras_copy():
    temp_dir = os.path.join("tests", "test_extras_copy")
    extras = [
        {"copy": True, "src": "README.md", "dest": os.path.join(temp_dir, "index.md")},
        {
            "copy": False,
            "src": "README.md",
            "dest": os.path.join(temp_dir, "index2.md"),
        },
    ]
    copier = HomepageCopier()
    config = MkDocsConfig()

    copier.config["copy"] = False
    copier.config["extras"] = extras

    clean_up(temp_dir)
    os.makedirs(temp_dir)

    _ = copier.on_config(config)
    assert os.path.exists(extras[0]["dest"])
    assert not os.path.exists(extras[1]["dest"])

    copier.on_post_build(config)
    assert not os.path.exists(extras[0]["dest"])

    clean_up(temp_dir)


def test_clean_up_on_error():
    temp_dir = os.path.join("tests", "test_clean_up_on_error")
    src_file = "README.md"
    dest_file = os.path.join(temp_dir, "index.md")
    copier = HomepageCopier()

    copier.config["dest"] = dest_file
    copier.config["extras"] = []

    clean_up(temp_dir)
    os.makedirs(temp_dir)

    shutil.copyfile(src_file, dest_file)

    copier.on_build_error(Exception())
    assert not os.path.exists(dest_file)

    clean_up(temp_dir)
