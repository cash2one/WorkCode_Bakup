<?php

/**
 * This is the model class for table "version".
 *
 * The followings are the available columns in table 'version':
 * @property string $id
 * @property integer $platform
 * @property string $version
 * @property string $title
 * @property string $info
 * @property string $update_url
 * @property string $add_time
 * @property integer $force_update
 */
class Version extends CActiveRecord
{
	/**
	 * 
	 * @var unknown
	 */
	const PLATFORM_ANDROID = 1;
	const PLATFORM_IOS = 2;
	
	
	/**
	 * @return string the associated database table name
	 */
	public function tableName()
	{
		return 'version';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('add_time', 'default', 'value' => time()),
			array('version, info, update_url, add_time', 'required'),
			// The following rule is used by search().
			// @todo Please remove those attributes that should not be searched.
			array('id, platform, version, title, info, update_url, add_time, force_update', 'safe'),
		);
	}

	/**
	 * @return array relational rules.
	 */
	public function relations()
	{
		// NOTE: you may need to adjust the relation name and the related
		// class name for the relations automatically generated below.
		return array(
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'id' => 'ID',
			'platform' => 'Platform',
			'version' => 'Version',
			'title' => 'Title',
			'info' => 'Info',
			'update_url' => 'Update Url',
			'add_time' => 'Add Time',
			'force_update' => 'Force Update',
		);
	}

	/**
	 * Retrieves a list of models based on the current search/filter conditions.
	 *
	 * Typical usecase:
	 * - Initialize the model fields with values from filter form.
	 * - Execute this method to get CActiveDataProvider instance which will filter
	 * models according to data in model fields.
	 * - Pass data provider to CGridView, CListView or any similar widget.
	 *
	 * @return CActiveDataProvider the data provider that can return the models
	 * based on the search/filter conditions.
	 */
	public function search()
	{
		// @todo Please modify the following code to remove attributes that should not be searched.

		$criteria=new CDbCriteria;

		$criteria->compare('id',$this->id,true);
		$criteria->compare('platform',$this->platform);
		$criteria->compare('version',$this->version,true);
		$criteria->compare('title',$this->title,true);
		$criteria->compare('info',$this->info,true);
		$criteria->compare('update_url',$this->update_url,true);
		$criteria->compare('add_time',$this->add_time,true);
		$criteria->compare('force_update',$this->force_update);

		return new CActiveDataProvider($this, array(
			'criteria'=>$criteria,
		));
	}

	/**
	 * Returns the static model of the specified AR class.
	 * Please note that you should have this exact method in all your CActiveRecord descendants!
	 * @param string $className active record class name.
	 * @return Version the static model class
	 */
	public static function model($className=__CLASS__)
	{
		return parent::model($className);
	}
	
	/**
	 * 获取最新的一条更新
	 * @param unknown $platform Android OR Ios
	 * @param string 之前的版本
	 */
	public function getLatestOne($platform=self::PLATFORM_ANDROID, $beforeVersion)
	{
		$data = array();
		$sql = "SELECT * FROM `" . $this->tableName() . "` AS v WHERE v.platform={$platform} AND v.`version`>'{$beforeVersion}' LIMIT 1";
		$result = Yii::app()->db->createCommand($sql)->queryRow();
		if (!empty($result))
		{
			$data = array(
				'title' => $result['title'],
				'version' => $result['version'],
				'info' => $result['info'],
				'update_url' => $result['update_url'],
				'force_update' => $result['force_update']
			);
		}
		return $data;
	}
}
